from flask import Flask, render_template, jsonify

from scanners.ec2_scanner import scan_ec2
from scanners.ebs_scanner import scan_ebs
from scanners.eip_scanner import scan_eips
from scanners.s3_scanner import scan_s3

from reports.cost_calculator import estimate_cost

from datetime import datetime

app = Flask(__name__)


def _safe_scan(scanner_func, default=None):
    """Run a scanner and fall back to an empty list if AWS access fails."""
    try:
        result = scanner_func()
        return result if result is not None else (default or [])
    except Exception as exc:
        print(f"Scanner error in {scanner_func.__name__}: {exc}")
        return default or []


def get_dashboard_data():
    """
    Collect all cloud resource data.
    """

    ec2 = _safe_scan(scan_ec2, [])
    ebs = _safe_scan(scan_ebs, [])
    eips = _safe_scan(scan_eips, [])
    s3 = _safe_scan(scan_s3, [])

    cost = estimate_cost(ebs, eips, ec2)

    health_score = max(
        0,
        100 - (
            len(ebs) * 10 +
            len(eips) * 5 +
            len(ec2) * 3
        )
    )

    if health_score >= 90:
        health_status = "Excellent"
        health_color = "green"

    elif health_score >= 70:
        health_status = "Good"
        health_color = "orange"

    else:
        health_status = "Needs Attention"
        health_color = "red"

    return {
        "ec2": ec2,
        "ebs": ebs,
        "eips": eips,
        "s3": s3,
        "cost": cost,

        "ec2_count": len(ec2),
        "ebs_count": len(ebs),
        "eips_count": len(eips),
        "s3_count": len(s3),

        "health_score": health_score,
        "health_status": health_status,
        "health_color": health_color,

        "last_scan": datetime.now().strftime("%d %b %Y  %I:%M:%S %p")
    }


@app.route("/")
def dashboard():

    data = get_dashboard_data()

    return render_template(
        "index.html",
        **data
    )


@app.route("/refresh")
def refresh():

    """
    Returns fresh scan data for JavaScript.
    """

    data = get_dashboard_data()

    return jsonify({
        "ec2_count": data["ec2_count"],
        "ebs_count": data["ebs_count"],
        "eips_count": data["eips_count"],
        "s3_count": data["s3_count"],

        "health_score": data["health_score"],
        "health_status": data["health_status"],

        "estimated_savings": data["cost"]["total"],

        "last_scan": data["last_scan"]
    })


@app.route("/api/chart")
def chart_data():

    """
    Chart.js data endpoint.
    """

    data = get_dashboard_data()

    return jsonify({

        "labels": [
            "EC2",
            "EBS",
            "Elastic IP",
            "S3"
        ],

        "values": [

            data["ec2_count"],
            data["ebs_count"],
            data["eips_count"],
            data["s3_count"]

        ]
    })


if __name__ == "__main__":

    app.run(
        debug=True,
        host="0.0.0.0",
        port=5000
    )