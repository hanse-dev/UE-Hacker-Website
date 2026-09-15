# Beispiel 2: Spiel - Leben und Energie
print("=== Beispiel 2: Spiel-Schleife ===")
leben = 100
runde = 1

while leben > 0:
    schaden = 20
    leben -= schaden
    print(f"Runde {runde}: -{schaden} Leben, übrig: {leben}")
    runde += 1

print(f"\n💀 Spiel vorbei nach {runde-1} Runden!")