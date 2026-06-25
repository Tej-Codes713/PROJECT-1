import boto3

def scan_ebs():

    ec2 = boto3.client("ec2", region_name="eu-north-1")

    response = ec2.describe_volumes()

    volumes = []

    for volume in response["Volumes"]:

        if len(volume["Attachments"]) == 0:

            volumes.append({
                "volume_id": volume["VolumeId"],
                "size": volume["Size"],
                "region": "eu-north-1"
            })

    return volumes