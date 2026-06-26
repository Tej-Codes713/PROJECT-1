import boto3
from scanners.regions import REGIONS

def scan_eips():

    eips = []

    for region in REGIONS:

        ec2 = boto3.client("ec2", region_name=region)

        response = ec2.describe_addresses()

        for address in response["Addresses"]:

            if "InstanceId" not in address:

                eips.append({
                    "ip": address["PublicIp"],
                    "region": region
                })

    return eips