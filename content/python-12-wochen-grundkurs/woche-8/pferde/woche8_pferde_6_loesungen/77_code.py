pferde = [
    {"name": "Blitz", "rasse": "Hannoveraner", "alter": 8, "punkte": 120},
    {"name": "Sturm", "rasse": "Haflinger", "alter": 12, "punkte": 150},
    {"name": "Luna", "rasse": "Isländer", "alter": 6, "punkte": 90},
    {"name": "Wind", "rasse": "Hannoveraner", "alter": 7, "punkte": 110},
]
alter_werte = [h["alter"] for h in pferde]
rangliste = sorted(alter_werte, reverse=True)
bester = pferde[0]
for h in pferde:
    if h["alter"] > bester["alter"]:
        bester = h
print(f"Bester: {bester['name']}")
print(f"Rangliste: {rangliste}")
