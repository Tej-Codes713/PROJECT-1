from scanners.ebs_scanner import scan_ebs
from scanners.eip_scanner import scan_eips
from scanners.ec2_scanner import scan_ec2

from reports.cost_calculator import estimate_cost


def generate_report():

    volumes = scan_ebs()
    eips = scan_eips()
    instances = scan_ec2()

    cost = estimate_cost(volumes, eips, instances)

    return {
        "unused_ebs_volumes": len(volumes),
        "unused_elastic_ips": len(eips),
        "idle_ec2_instances": len(instances),

        "ebs_monthly_cost": cost["ebs_cost"],
        "eip_monthly_cost": cost["eip_cost"],
        "ec2_monthly_cost": cost["ec2_cost"],

        "estimated_monthly_savings": cost["total"]
    }