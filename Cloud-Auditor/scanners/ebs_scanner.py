def scan_ebs():
    volumes = [
        {
            "volume_id": "vol-12345",
            "size": 100,
            "region": "ap-south-1"
        },
        {
            "volume_id": "vol-67890",
            "size": 50,
            "region": "us-east-1"
        }
    ]

    return volumes