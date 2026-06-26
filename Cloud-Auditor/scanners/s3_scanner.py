import boto3


def scan_s3():

    s3 = boto3.client("s3")

    response = s3.list_buckets()

    buckets = []

    for bucket in response.get("Buckets", []):

        buckets.append({
            "bucket_name": bucket["Name"],
            "created": bucket["CreationDate"].strftime("%Y-%m-%d")
        })

    return buckets