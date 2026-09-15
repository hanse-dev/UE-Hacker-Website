# Sensor-Arrays als Dictionary of Dictionaries
sensoren = {
    "Langstrecken-Radar": {"techniker": "Lt. Vex", "status": "aktiv", "reichweite": 100},
    "Nahbereichs-Scanner": {"techniker": "Ens. Pryn", "status": "wartung", "reichweite": 60},
    "Spektralanalyse": {"techniker": "Dr. Aiko", "status": "aktiv", "reichweite": 85},
}

print("=== Sensor-Matrix ===")
for name, daten in sensoren.items():
    symbol = "✅" if daten["status"] == "aktiv" else "⚠️"
    print(f"  {symbol} {name}: Techniker: {daten['techniker']}, Reichweite: {daten['reichweite']}%")

# Wartungsbedürftige Arrays
wartung_noetig = {k: v for k, v in sensoren.items() if v["reichweite"] < 80}
print(f"\nWartungsbedürftige Arrays: {list(wartung_noetig.keys())}")

# Reichweiten-Durchschnitt
avg = sum(v["reichweite"] for v in sensoren.values()) / len(sensoren)
print(f"Durchschnittliche Reichweite: {avg:.1f}%")
