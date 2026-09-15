# Beispiel 2: Liste von Stallkarten
pferde = [
    {
        "name": "Thunder",
        "rasse": "Hannoveraner",
        "alter": 8,
        "trainingslevel": "M"
    },
    {
        "name": "Luna",
        "rasse": "Isländer",
        "alter": 6,
        "trainingslevel": "A"
    },
    {
        "name": "Stormy",
        "rasse": "Quarter Horse",
        "alter": 10,
        "trainingslevel": "L"
    }
]

print("=== Pferde-Liste ===")
for pferd in pferde:
    print(f"{pferd['name']} - {pferd['rasse']} ({pferd['alter']} Jahre)")

# Nach Alter filtern
junge = [p for p in pferde if p['alter'] < 8]
print(f"\nJunge Pferde: {[p['name'] for p in junge]}")