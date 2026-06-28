import boto3
from botocore.exceptions import ClientError


def scan_iam():
    """
    Scan IAM Users in the AWS account.
    Returns:
        List of IAM users with:
        - User Name
        - Creation Date
        - Console Login (Yes/No)
    """

    iam = boto3.client("iam")

    users = []

    try:
        response = iam.list_users()

        for user in response.get("Users", []):

            username = user["UserName"]

            created = user["CreateDate"].strftime("%Y-%m-%d")

            console_login = "No"

            try:
                iam.get_login_profile(UserName=username)
                console_login = "Yes"

            except ClientError:
                console_login = "No"

            users.append(
                {
                    "user_name": username,
                    "created": created,
                    "console_login": console_login,
                }
            )

    except ClientError as e:
        print(f"IAM Scan Error: {e}")

    return users