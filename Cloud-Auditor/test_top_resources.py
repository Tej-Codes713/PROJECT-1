from recommendations.top_resources import get_top_costly_resources

resources = get_top_costly_resources()

for resource in resources:
    print(resource)