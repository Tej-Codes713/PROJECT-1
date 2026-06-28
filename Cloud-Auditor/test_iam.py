from scanners.iam_scanner import scan_iam

users = scan_iam()

print(users)