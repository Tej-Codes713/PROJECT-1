import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from scanners.ebs_scanner import scan_ebs
from scanners.eip_scanner import scan_eips
from scanners.ec2_scanner import scan_ec2


def test_ebs_scanner():
    result = scan_ebs()
    assert len(result) > 0


def test_eip_scanner():
    result = scan_eips()
    assert len(result) > 0


def test_ec2_scanner():
    result = scan_ec2()
    assert len(result) > 0