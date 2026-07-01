import boto3
from botocore.exceptions import ClientError


def scan_s3():
    buckets = []

    try:
        s3 = boto3.client("s3")
        response = s3.list_buckets()
    except ClientError as exc:
        if exc.response.get("Error", {}).get("Code") in {"AuthFailure", "AuthorizationHeaderMalformed"}:
            print("Skipping S3 scan: AWS credentials are not configured correctly.")
            return []
        raise

    for bucket in response.get("Buckets", []):
        buckets.append({
            "bucket_name": bucket["Name"],
            "created": bucket["CreationDate"].strftime("%Y-%m-%d")
        })

    return buckets