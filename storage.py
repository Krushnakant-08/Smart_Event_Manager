import json
FILE = "events.json"

def load_events():
    try:
        with open(FILE, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def save_events(events):
    with open(FILE, "w") as f:
        json.dump(events, f, indent=4)