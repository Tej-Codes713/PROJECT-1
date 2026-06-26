import typer
from rich.console import Console
from rich.table import Table

from scanners.ebs_scanner import scan_ebs
from scanners.eip_scanner import scan_eips
from scanners.ec2_scanner import scan_ec2
from scanners.s3_scanner import scan_s3

from reports.report_generator import generate_report
from reports.exporter import export_json, export_csv

from cleanup.cleanup_manager import run_cleanup

app = typer.Typer()
console = Console()


@app.command()
def scan():

    # -----------------------------
    # EBS Scanner
    # -----------------------------
    volumes = scan_ebs()

    ebs_table = Table(title="Unused EBS Volumes")
    ebs_table.add_column("Volume ID")
    ebs_table.add_column("Size (GB)")
    ebs_table.add_column("Region")

    for volume in volumes:
        ebs_table.add_row(
            volume["volume_id"],
            str(volume["size"]),
            volume["region"]
        )

    console.print(ebs_table)

    # -----------------------------
    # Elastic IP Scanner
    # -----------------------------
    eips = scan_eips()

    eip_table = Table(title="Unused Elastic IPs")
    eip_table.add_column("IP Address")
    eip_table.add_column("Region")

    for eip in eips:
        eip_table.add_row(
            eip["ip"],
            eip["region"]
        )

    console.print(eip_table)

    # -----------------------------
    # EC2 Scanner
    # -----------------------------
    instances = scan_ec2()

    ec2_table = Table(title="Underutilized EC2 Instances")
    ec2_table.add_column("Instance ID")
    ec2_table.add_column("CPU Usage")
    ec2_table.add_column("Region")

    for instance in instances:
        ec2_table.add_row(
            instance["instance_id"],
            instance["cpu_usage"],
            instance["region"]
        )

    console.print(ec2_table)

    # -----------------------------
    # S3 Scanner
    # -----------------------------
    buckets = scan_s3()

    s3_table = Table(title="S3 Buckets")
    s3_table.add_column("Bucket Name")
    s3_table.add_column("Created On")

    for bucket in buckets:
        s3_table.add_row(
            bucket["bucket_name"],
            bucket["created"]
        )

    console.print(s3_table)


@app.command()
def report():

    report_data = generate_report()

    print("\n========== Cloud Audit Report ==========\n")

    print(
        f"Unused EBS Volumes : {report_data['unused_ebs_volumes']} "
        f"(${report_data['ebs_monthly_cost']}/month)"
    )

    print(
        f"Unused Elastic IPs : {report_data['unused_elastic_ips']} "
        f"(${report_data['eip_monthly_cost']}/month)"
    )

    print(
        f"Idle EC2 Instances : {report_data['idle_ec2_instances']} "
        f"(${report_data['ec2_monthly_cost']}/month)"
    )

    print("----------------------------------------")

    print(
        f"Estimated Monthly Savings : "
        f"${report_data['estimated_monthly_savings']}/month"
    )

    export_json(report_data)
    export_csv(report_data)


@app.command()
def cleanup():
    run_cleanup()


if __name__ == "__main__":
    app()