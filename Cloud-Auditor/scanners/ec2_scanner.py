import boto3
from datetime import datetime, timedelta

def scan_ec2():

    ec2 = boto3.client("ec2", region_name="eu-north-1")
    cloudwatch = boto3.client("cloudwatch", region_name="eu-north-1")

    response = ec2.describe_instances()

    instances = []

    for reservation in response["Reservations"]:
        for instance in reservation["Instances"]:

            instance_id = instance["InstanceId"]

            metrics = cloudwatch.get_metric_statistics(
                Namespace="AWS/EC2",
                MetricName="CPUUtilization",
                Dimensions=[
                    {
                        "Name": "InstanceId",
                        "Value": instance_id
                    }
                ],
                StartTime=datetime.utcnow() - timedelta(hours=1),
                EndTime=datetime.utcnow(),
                Period=300,
                Statistics=["Average"]
            )

            datapoints = metrics["Datapoints"]

            if datapoints:
                cpu = round(datapoints[-1]["Average"], 2)
            else:
                cpu = 0

            instances.append({
                "instance_id": instance_id,
                "cpu_usage": f"{cpu}%",
                "region": "eu-north-1"
            })

    return instances