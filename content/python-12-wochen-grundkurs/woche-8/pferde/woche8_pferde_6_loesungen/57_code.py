pferde = [
    {"name": "Blitz", "rasse": "Hannoveraner", "alter": 8, "punkte": 120},
    {"name": "Sturm", "rasse": "Haflinger", "alter": 12, "punkte": 150},
    {"name": "Luna", "rasse": "Isländer", "alter": 6, "punkte": 90},
    {"name": "Wind", "rasse": "Hannoveraner", "alter": 7, "punkte": 110},
]
summe = 0
for h in pferde:
    summe += h["alter"]
durchschnitt = summe / len(pferde)
print(f"Durchschnitt: {durchschnitt}")
