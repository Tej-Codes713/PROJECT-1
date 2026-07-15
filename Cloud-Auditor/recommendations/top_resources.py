from scanners.ec2_scanner import scan_ec2
from scanners.ebs_scanner import scan_ebs
from scanners.eip_scanner import scan_eips


def get_top_costly_resources():
    """
    Returns the most expensive AWS resources.
    """

    resources = []

    # -----------------------------
    # EC2 Instances
    # -----------------------------
    ec2 = scan_ec2()

    for instance in ec2:

        resources.append({
            "type": "EC2 Instance",
            "id": instance["instance_id"],
            "region": instance["region"],
            "monthly_cost": 15
        })

    # -----------------------------
    # Unused EBS Volumes
    # -----------------------------
    ebs = scan_ebs()

    for volume in ebs:

        resources.append({
            "type": "EBS Volume",
            "id": volume["volume_id"],
            "region": volume["region"],
            "monthly_cost": 8
        })

    # -----------------------------
    # Elastic IPs
    # -----------------------------
    eips = scan_eips()

    for ip in eips:

        resources.append({
            "type": "Elastic IP",
            "id": ip["ip"],
            "region": ip["region"],
            "monthly_cost": 3
        })

    # Highest cost first
    resources.sort(
        key=lambda x: x["monthly_cost"],
        reverse=True
    )

    return resources[:10]