import json

def laden(filename):
    try:
        with open(filename, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        print("📂 Es gibt noch keinen Spielstand.")
        return None

laden("gibtsnicht.json")
