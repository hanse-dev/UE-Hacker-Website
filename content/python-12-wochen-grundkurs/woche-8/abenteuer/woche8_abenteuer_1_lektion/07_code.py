held = {
    "name": "Aria",
    "klasse": "Magierin",
    "level": 15,
    "lebenspunkte": 120
}

# .keys() – nur Schlüssel
print("Eigenschaften:", list(held.keys()))

# .values() – nur Werte
print("Werte:", list(held.values()))

# .items() – Schlüssel + Wert
print("\n=== Helden-Steckbrief ===")
for eigenschaft, wert in held.items():
    print(f"  {eigenschaft}: {wert}")
