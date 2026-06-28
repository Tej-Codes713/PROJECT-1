from scanners.ebs_scanner import scan_ebs
from scanners.eip_scanner import scan_eips
from scanners.ec2_scanner import scan_ec2
from scanners.s3_scanner import scan_s3
from scanners.iam_scanner import scan_iam

from reports.cost_calculator import estimate_cost


def generate_report():
    """
    Generate a complete cloud audit report.
    """

    # Scan AWS Resources
    volumes = scan_ebs()
    eips = scan_eips()
    instances = scan_ec2()
    buckets = scan_s3()
    users = scan_iam()

    # Calculate estimated monthly savings
    cost = estimate_cost(volumes, eips, instances)

    report = {
        "unused_ebs_volumes": len(volumes),
        "unused_elastic_ips": len(eips),
        "idle_ec2_instances": len(instances),
        "s3_buckets": len(buckets),
        "iam_users": len(users),

        "ebs_monthly_cost": cost["ebs_cost"],
        "eip_monthly_cost": cost["eip_cost"],
        "ec2_monthly_cost": cost["ec2_cost"],

        "estimated_monthly_savings": cost["total"],

        # Optional: Detailed resources
        "resources": {
            "ebs": volumes,
            "elastic_ips": eips,
            "ec2_instances": instances,
            "s3_buckets": buckets,
            "iam_users": users,
        }
    }

    return report