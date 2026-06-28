from scanners.ec2_scanner import scan_ec2
from scanners.ebs_scanner import scan_ebs
from scanners.eip_scanner import scan_eips
from scanners.s3_scanner import scan_s3
from scanners.iam_scanner import scan_iam


def generate_ai_recommendations():
    """
    Generate intelligent cloud optimization recommendations.
    """

    recommendations = []
    total_savings = 0

    # ===========================
    # EC2 Recommendations
    # ===========================
    ec2_instances = scan_ec2()

    for instance in ec2_instances:

        cpu = float(instance["cpu_usage"].replace("%", ""))

        if cpu < 5:

            savings = 15

            total_savings += savings

            recommendations.append({
                "resource": "EC2 Instance",
                "id": instance["instance_id"],
                "action": "Terminate or Downsize",
                "reason": f"CPU utilization is only {instance['cpu_usage']}",
                "estimated_savings": savings
            })

    # ===========================
    # EBS Recommendations
    # ===========================
    ebs_volumes = scan_ebs()

    for volume in ebs_volumes:

        savings = 8

        total_savings += savings

        recommendations.append({
            "resource": "EBS Volume",
            "id": volume["volume_id"],
            "action": "Delete",
            "reason": "Volume is unattached.",
            "estimated_savings": savings
        })

    # ===========================
    # Elastic IP Recommendations
    # ===========================
    elastic_ips = scan_eips()

    for ip in elastic_ips:

        savings = 3

        total_savings += savings

        recommendations.append({
            "resource": "Elastic IP",
            "id": ip["ip"],
            "action": "Release",
            "reason": "Elastic IP is unused.",
            "estimated_savings": savings
        })

    # ===========================
    # S3 Recommendations
    # ===========================
    buckets = scan_s3()

    if len(buckets) > 20:

        recommendations.append({
            "resource": "S3",
            "id": "-",
            "action": "Review Storage",
            "reason": "Large number of S3 buckets detected.",
            "estimated_savings": 0
        })

    # ===========================
    # IAM Recommendations
    # ===========================
    users = scan_iam()

    if len(users) > 10:

        recommendations.append({
            "resource": "IAM",
            "id": "-",
            "action": "Audit Users",
            "reason": "Too many IAM users exist.",
            "estimated_savings": 0
        })

    # ===========================
    # Overall Recommendation
    # ===========================
    if total_savings == 0:

        summary = (
            "Excellent! No major cost optimization opportunities were detected."
        )

    else:

        summary = (
            f"You can save approximately ${total_savings}/month by following "
            f"the recommended actions."
        )

    return {
        "recommendations": recommendations,
        "total_savings": total_savings,
        "summary": summary
    }