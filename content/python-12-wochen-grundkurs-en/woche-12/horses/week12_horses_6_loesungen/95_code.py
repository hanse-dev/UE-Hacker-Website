import json

def load_state(filename):
    try:
        with open(filename, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

print(f"Count: {len(load_state('missing.json'))}")
