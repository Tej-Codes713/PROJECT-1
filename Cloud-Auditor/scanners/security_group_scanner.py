import boto3
from scanners.regions import REGIONS


def scan_security_groups():

    unused_groups = []

    for region in REGIONS:

        ec2 = boto3.client("ec2", region_name=region)

        security_groups = ec2.describe_security_groups()["SecurityGroups"]

        network_interfaces = ec2.describe_network_interfaces()["NetworkInterfaces"]

        used_groups = set()

        for eni in network_interfaces:
            for group in eni["Groups"]:
                used_groups.add(group["GroupId"])

        for sg in security_groups:

            if sg["GroupName"] == "default":
                continue

            if sg["GroupId"] not in used_groups:

                unused_groups.append({
                    "group_id": sg["GroupId"],
                    "group_name": sg["GroupName"],
                    "region": region
                })

    return unused_groups