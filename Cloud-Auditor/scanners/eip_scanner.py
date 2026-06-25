import boto3

def scan_eips():

    ec2 = boto3.client("ec2", region_name="eu-north-1")

    response = ec2.describe_addresses()

    eips = []

    for address in response["Addresses"]:

        if "InstanceId" not in address:

            eips.append({
                "ip": address["PublicIp"],
                "region": "eu-north-1"
            })

    return eips