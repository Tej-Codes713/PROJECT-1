import boto3
from botocore.exceptions import ClientError

from scanners.regions import REGIONS


def scan_eips():
    eips = []

    for region in REGIONS:
        try:
            ec2 = boto3.client("ec2", region_name=region)
            response = ec2.describe_addresses()
        except ClientError as exc:
            if exc.response.get("Error", {}).get("Code") == "AuthFailure":
                print(f"Skipping EIP scan in {region}: AWS credentials are not configured correctly.")
                continue
            raise

        for address in response.get("Addresses", []):
            if "InstanceId" not in address:
                eips.append({
                    "ip": address["PublicIp"],
                    "region": region,
                })

    return eips