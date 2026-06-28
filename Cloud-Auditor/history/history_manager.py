import json
import os
from datetime import datetime

HISTORY_FILE = "history/scan_history.json"

def save_scan(report):
    """
    Save the current scan into history.
    """

    if not os.path.exists(HISTORY_FILE):

        with open(HISTORY_FILE, "w") as file:
            json.dump([], file)

    with open(HISTORY_FILE, "r") as file:

        history = json.load(file)

    history.insert(0, {

        "time": datetime.now().strftime("%d-%b-%Y %I:%M %p"),

        "resources": report["resources"],

        "monthly_savings": report["monthly_savings"],

        "health": report["health"]

    })

    history = history[:20]

    with open(HISTORY_FILE, "w") as file:

        json.dump(history, file, indent=4)

def load_history():

    if not os.path.exists(HISTORY_FILE):
        return []

    with open(HISTORY_FILE, "r") as file:

        return json.load(file)
