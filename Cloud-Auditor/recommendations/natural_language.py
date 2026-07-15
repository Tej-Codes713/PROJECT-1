def process_query(query):
    """
    Process simple natural language commands.
    """

    query = query.lower().strip()

    if "ec2" in query:
        return "ec2"

    elif "ebs" in query:
        return "ebs"

    elif "elastic" in query or "eip" in query:
        return "eips"

    elif "s3" in query:
        return "s3"

    elif "iam" in query:
        return "iam"

    elif "all" in query:
        return "all"

    return "all"