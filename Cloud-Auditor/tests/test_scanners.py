import sys
import os

from botocore.exceptions import ClientError

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from scanners.ebs_scanner import scan_ebs
from scanners.eip_scanner import scan_eips
from scanners.ec2_scanner import scan_ec2
from scanners.s3_scanner import scan_s3


def test_ebs_scanner():
    result = scan_ebs()
    assert len(result) > 0


def test_ebs_scanner_handles_auth_failure(monkeypatch):
    def fail_client(*args, **kwargs):
        raise ClientError(
            {"Error": {"Code": "AuthFailure", "Message": "invalid credentials"}},
            "DescribeVolumes",
        )

    monkeypatch.setattr("scanners.ebs_scanner.boto3.client", fail_client)

    assert scan_ebs() == []


def test_eip_scanner():
    result = scan_eips()
    assert len(result) > 0


def test_ec2_scanner():
    result = scan_ec2()
    assert len(result) > 0


def test_s3_scanner_handles_auth_failure(monkeypatch):
    def fail_client(*args, **kwargs):
        raise ClientError(
            {"Error": {"Code": "AuthorizationHeaderMalformed", "Message": "invalid credentials"}},
            "ListBuckets",
        )

    monkeypatch.setattr("scanners.s3_scanner.boto3.client", fail_client)

    assert scan_s3() == []