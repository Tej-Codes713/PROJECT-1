import json

def export_json(report_data):

    with open("report.json", "w") as file:
        json.dump(report_data, file, indent=4)

    print("\nReport saved as report.json")

import csv

def export_csv(report_data):

    with open("report.csv", "w", newline="") as file:

        writer = csv.writer(file)

        writer.writerow(["Metric", "Value"])

        writer.writerow(["Unused EBS Volumes", report_data["unused_ebs_volumes"]])

        writer.writerow(["Unused Elastic IPs", report_data["unused_elastic_ips"]])

        writer.writerow(["Idle EC2 Instances", report_data["idle_ec2_instances"]])

        writer.writerow(["Estimated Monthly Savings", report_data["estimated_monthly_savings"]])

    print("CSV Report saved!")