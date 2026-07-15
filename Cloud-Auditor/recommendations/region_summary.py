from collections import defaultdict


def build_region_summary(ec2, ebs, eips, s3, iam):
    """
    Create a summary of AWS resources grouped by region.
    """

    regions = defaultdict(lambda: {
        "ec2": 0,
        "ebs": 0,
        "eips": 0,
        "s3": 0,
        "iam": 0,
        "status": "Healthy"
    })

    # -----------------------
    # EC2
    # -----------------------
    for instance in ec2:

        region = instance.get("region", "Unknown")

        regions[region]["ec2"] += 1

    # -----------------------
    # EBS
    # -----------------------
    for volume in ebs:

        region = volume.get("region", "Unknown")

        regions[region]["ebs"] += 1

    # -----------------------
    # Elastic IP
    # -----------------------
    for ip in eips:

        region = ip.get("region", "Unknown")

        regions[region]["eips"] += 1

    # -----------------------
    # S3
    # -----------------------
    for bucket in s3:

        region = bucket.get("region", "Global")

        regions[region]["s3"] += 1

    # -----------------------
    # IAM
    # IAM is global, so assign to Global
    # -----------------------
    regions["Global"]["iam"] = len(iam)

    # -----------------------
    # Health Status
    # -----------------------
    for region in regions:

        data = regions[region]

        issues = (
            data["ebs"]
            + data["eips"]
        )

        if issues >= 5:

            data["status"] = "Critical"

        elif issues >= 2:

            data["status"] = "Needs Attention"

        else:

            data["status"] = "Healthy"

    return dict(regions)