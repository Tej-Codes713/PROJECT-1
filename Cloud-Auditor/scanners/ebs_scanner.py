import boto3
from scanners.regions import REGIONS

def scan_ebs():

    volumes = []

    for region in REGIONS:

        ec2 = boto3.client("ec2", region_name=region)

        response = ec2.describe_volumes()

        for volume in response["Volumes"]:

            if len(volume["Attachments"]) == 0:

                volumes.append({
                    "volume_id": volume["VolumeId"],
                    "size": volume["Size"],
                    "region": region
                })

    return volumes