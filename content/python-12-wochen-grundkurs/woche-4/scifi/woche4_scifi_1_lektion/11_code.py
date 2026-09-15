# Beispiel 2: Schild-Generator
print("=== Beispiel 2: Schild-Generator ===")
energie = 100
minute = 1

while energie > 20:
    verbrauch = 15
    energie -= verbrauch
    print(f"Minute {minute}: -{verbrauch} Energie, übrig: {energie}%")
    minute += 1

print(f"\n⚠️ Schild-Kritisch nach {minute-1} Minuten!")
print("Energie nachladen!")