from scanners.security_group_scanner import scan_security_groups
from scanners.iam_scanner import scan_iam
from scanners.s3_scanner import scan_s3


def security_center():

    security_groups = scan_security_groups()
    iam_users = scan_iam()
    buckets = scan_s3()

    findings = []

    # -------------------------
    # Open Security Groups
    # -------------------------

    if len(security_groups) > 0:

        findings.append({

            "title": "Open Security Groups",

            "count": len(security_groups),

            "status": "Warning"

        })

    else:

        findings.append({

            "title": "Open Security Groups",

            "count": 0,

            "status": "Good"

        })

    # -------------------------
    # IAM Users
    # -------------------------

    findings.append({

        "title": "IAM Users",

        "count": len(iam_users),

        "status": "Info"

    })

    # -------------------------
    # S3 Buckets
    # -------------------------

    findings.append({

        "title": "S3 Buckets",

        "count": len(buckets),

        "status": "Info"

    })

    recommendations = [

        "Close unnecessary Security Group ports",

        "Enable MFA for IAM Users",

        "Review IAM permissions",

        "Delete unused Security Groups",

        "Review S3 Bucket permissions"

    ]

    return {

        "findings": findings,

        "recommendations": recommendations

    }