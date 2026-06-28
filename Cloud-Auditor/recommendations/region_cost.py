from scanners.ec2_scanner import scan_ec2
from scanners.ebs_scanner import scan_ebs
from scanners.eip_scanner import scan_eips


def region_cost_breakdown():

    region_cost = {}

    # -------------------------
    # EC2
    # -------------------------

    for instance in scan_ec2():

        region = instance["region"]

        region_cost.setdefault(region, 0)

        region_cost[region] += 15

    # -------------------------
    # EBS
    # -------------------------

    for volume in scan_ebs():

        region = volume["region"]

        region_cost.setdefault(region, 0)

        region_cost[region] += 8

    # -------------------------
    # Elastic IP
    # -------------------------

    for ip in scan_eips():

        region = ip["region"]

        region_cost.setdefault(region, 0)

        region_cost[region] += 3

    return region_cost