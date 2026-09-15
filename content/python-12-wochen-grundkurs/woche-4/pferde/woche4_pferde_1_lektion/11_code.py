# Beispiel 2: Pferd-Training
print("=== Beispiel 2: Training bis zur Erschöpfung ===")
ausdauer = 100
runde = 1

while ausdauer > 20:
    verbrauch = 15
    ausdauer -= verbrauch
    print(f"Runde {runde}: -{verbrauch} Ausdauer, übrig: {ausdauer}%")
    runde += 1

print(f"\n💪 Training beendet nach {runde-1} Runden!")
print("Zeit für eine Pause!")