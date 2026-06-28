from recommendations.risk_score import calculate_risk_score
from recommendations.cost_prediction import predict_next_month_cost


def executive_dashboard(ec2, ebs, eips, s3, iam):
    """
    Build Executive KPI Dashboard
    """

    risk = calculate_risk_score()
    prediction = predict_next_month_cost()

    total_resources = (
        len(ec2)
        + len(ebs)
        + len(eips)
        + len(s3)
        + len(iam)
    )

    return {

        "total_resources": total_resources,

        "regions": 4,

        "ec2": len(ec2),

        "ebs": len(ebs),

        "eips": len(eips),

        "s3": len(s3),

        "iam": len(iam),

        "monthly_savings": prediction["current"],

        "predicted_cost": prediction["predicted"],

        "risk_score": risk["score"],

        "risk_level": risk["level"]

    }