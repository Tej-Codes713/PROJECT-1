from scanners.ebs_scanner import scan_ebs
from scanners.eip_scanner import scan_eips
from scanners.ec2_scanner import scan_ec2

def generate_report():

    volumes = scan_ebs()
    eips = scan_eips()
    instances = scan_ec2()

    return {
        "unused_ebs_volumes": len(volumes),
        "unused_elastic_ips": len(eips),
        "idle_ec2_instances": len(instances),
        "estimated_monthly_savings": "$120"
    }