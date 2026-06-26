import boto3
from datetime import datetime, timedelta

from scanners.regions import REGIONS


def scan_ec2():
    """Scan EC2 instances across supported regions and return CPU metrics."""
    instances = []

    for region in REGIONS:
        ec2 = boto3.client("ec2", region_name=region)
        cloudwatch = boto3.client("cloudwatch", region_name=region)

        response = ec2.describe_instances()

        for reservation in response.get("Reservations", []):
            for instance in reservation.get("Instances", []):
                instance_id = instance.get("InstanceId")
                if not instance_id:
                    continue

                metrics = cloudwatch.get_metric_statistics(
                    Namespace="AWS/EC2",
                    MetricName="CPUUtilization",
                    Dimensions=[
                        {
                            "Name": "InstanceId",
                            "Value": instance_id,
                        }
                    ],
                    StartTime=datetime.utcnow() - timedelta(hours=1),
                    EndTime=datetime.utcnow(),
                    Period=300,
                    Statistics=["Average"],
                )

                datapoints = metrics.get("Datapoints", [])
                cpu = round(datapoints[-1]["Average"], 2) if datapoints else 0

                # Only report idle instances
                if cpu < 5:
                    instances.append({
                        "instance_id": instance_id,
                        "cpu_usage": f"{cpu}%",
                        "region": region,
                    })

    return instances
