from flask import Flask, render_template
from datetime import datetime

from scanners.ec2_scanner import scan_ec2
from scanners.ebs_scanner import scan_ebs
from scanners.eip_scanner import scan_eips
from scanners.s3_scanner import scan_s3
from scanners.iam_scanner import scan_iam

from reports.cost_calculator import estimate_cost
from recommendations.ai_recommendations import generate_ai_recommendations
from recommendations.risk_score import calculate_risk_score
from recommendations.cost_prediction import predict_next_month_cost
from recommendations.executive_dashboard import executive_dashboard
from flask import request
from recommendations.natural_language import process_query
from recommendations.region_summary import build_region_summary
from recommendations.top_resources import get_top_costly_resources
from history.history_manager import save_scan, load_history
from recommendations.security_center import security_center
from recommendations.region_cost import region_cost_breakdown


app = Flask(__name__)


@app.route("/")
def home():

    # ===============================
    # AWS Scanners
    # ===============================

    ec2 = scan_ec2()
    ebs = scan_ebs()
    eips = scan_eips()
    s3 = scan_s3()
    iam = scan_iam()

    region_summary = build_region_summary(
    ec2,
    ebs,
    eips,
    s3,
    iam
)
    
    # ===============================
    # Cost
    # ===============================

    cost = estimate_cost(ebs, eips, ec2)

    # ===============================
    # AI Recommendations
    # ===============================

    ai = generate_ai_recommendations()
    risk = calculate_risk_score()
    prediction = predict_next_month_cost()
    dashboard = executive_dashboard(
    ec2,
    ebs,
    eips,
    s3,
    iam
)
    top_resources = get_top_costly_resources()
    security = security_center()
    region_cost = region_cost_breakdown()

    # ===============================
    # Health Score
    # ===============================

    issues = len(ec2) + len(ebs) + len(eips)

    health_score = max(100 - (issues * 5), 50)

    if health_score >= 90:
        health_status = "Excellent"

    elif health_score >= 75:
        health_status = "Good"

    else:
        health_status = "Needs Attention"

    # =====================================
    # Scan History
    # =====================================

    report = {

        "resources": dashboard["total_resources"],

        "monthly_savings": dashboard["monthly_savings"],

        "health": health_score

    }

    save_scan(report)

    history = load_history()

    # ===============================
    # Last Scan
    # ===============================

    last_scan = datetime.now().strftime("%d-%m-%Y %H:%M:%S")

    query = request.args.get("search", "")
    selected = process_query(query)

    return render_template(

        "index.html",

        ec2=ec2,
        ebs=ebs,
        eips=eips,
        s3=s3,
        iam=iam,

        ec2_count=len(ec2),
        ebs_count=len(ebs),
        eips_count=len(eips),
        s3_count=len(s3),
        iam_count=len(iam),

        cost=cost,
        region_cost=region_cost,

        ai=ai,
        prediction=prediction,
        risk=risk,
        dashboard=dashboard,
        region_summary=region_summary,
        top_resources=top_resources,
       
        history=history,
        security=security,

        health_score=health_score,
        health_status=health_status,

        query=query,
        selected=selected,
        last_scan=last_scan

    )


if __name__ == "__main__":
    app.run(debug=True, port=1234)