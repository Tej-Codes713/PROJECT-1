from scanners.security_group_scanner import scan_security_groups
from scanners.s3_scanner import scan_s3
from scanners.iam_scanner import scan_iam


def calculate_risk_score():
    """
    Calculate a security risk score (0–10).
    """

    score = 10
    issues = []

    # ==========================
    # Security Groups
    # ==========================

    security_groups = scan_security_groups()

    if len(security_groups) > 0:
        deduction = min(len(security_groups), 3)
        score -= deduction

        issues.append(
            f"{len(security_groups)} Security Group(s) allow public access."
        )

    # ==========================
    # S3 Buckets
    # ==========================

    buckets = scan_s3()

    if len(buckets) > 20:

        score -= 2

        issues.append("Large number of S3 buckets detected.")

    # ==========================
    # IAM Users
    # ==========================

    users = scan_iam()

    if len(users) > 10:

        score -= 1

        issues.append("High number of IAM users.")

    # ==========================
    # Final Score
    # ==========================

    if score < 0:
        score = 0

    if score >= 8:
        level = "LOW"

    elif score >= 5:
        level = "MEDIUM"

    else:
        level = "HIGH"

    return {
        "score": score,
        "level": level,
        "issues": issues
    }