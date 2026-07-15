from reports.cost_calculator import estimate_cost
from scanners.ebs_scanner import scan_ebs
from scanners.eip_scanner import scan_eips
from scanners.ec2_scanner import scan_ec2


def predict_next_month_cost():
    """
    Predict next month's cloud cost based on current usage.
    """

    ebs = scan_ebs()
    eips = scan_eips()
    ec2 = scan_ec2()

    cost = estimate_cost(ebs, eips, ec2)

    current = cost["total"]

    # Assume 20% growth
    predicted = round(current * 1.20, 2)

    difference = predicted - current

    if difference > 0:
        trend = "Increase"
    elif difference < 0:
        trend = "Decrease"
    else:
        trend = "Stable"

    return {
        "current": current,
        "predicted": predicted,
        "difference": difference,
        "trend": trend
    }