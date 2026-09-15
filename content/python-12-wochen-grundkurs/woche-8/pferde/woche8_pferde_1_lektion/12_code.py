# Beispiel 1: Stallkarte in Stallkarte
stall = {
    "name": "Sonnental",
    "location": {
        "region": "Süddeutschland",
        "koordinaten": (100, 200),
        "bundesland": "Bayern"
    },
    "einrichtungen": {
        "reithalle": "20x40m",
        "reitplatz": "30x60m",
        "paddocks": "5 Stück"
    }
}

print("=== Verschachtelte Stallkarte ===")
print(f"Stall: {stall['name']}")
print(f"Region: {stall['location']['region']}")
print(f"Koordinaten: {stall['location']['koordinaten']}")
print(f"Reithalle: {stall['einrichtungen']['reithalle']}")