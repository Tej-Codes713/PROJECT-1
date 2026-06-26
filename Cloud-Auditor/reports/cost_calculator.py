def estimate_cost(volumes, eips, instances):
    """
    Estimate monthly savings based on unused AWS resources.
    """

    EBS_COST = 8      # $8 per unused EBS volume/month
    EIP_COST = 3      # $3 per unused Elastic IP/month
    EC2_COST = 15     # $15 per idle EC2/month

    ebs_cost = len(volumes) * EBS_COST
    eip_cost = len(eips) * EIP_COST
    ec2_cost = len(instances) * EC2_COST

    total = ebs_cost + eip_cost + ec2_cost

    return {
        "ebs_cost": ebs_cost,
        "eip_cost": eip_cost,
        "ec2_cost": ec2_cost,
        "total": total
    }