import boto3
from botocore.exceptions import ClientError

from scanners.regions import REGIONS


def scan_ebs():
    volumes = []

    for region in REGIONS:
        try:
            ec2 = boto3.client("ec2", region_name=region)
            response = ec2.describe_volumes()
        except ClientError as exc:
            if exc.response.get("Error", {}).get("Code") == "AuthFailure":
                print(f"Skipping EBS scan in {region}: AWS credentials are not configured correctly.")
                continue
            raise

        for volume in response.get("Volumes", []):
            if len(volume.get("Attachments", [])) == 0:
                volumes.append({
                    "volume_id": volume["VolumeId"],
                    "size": volume["Size"],
                    "region": region,
                })

    return volumes