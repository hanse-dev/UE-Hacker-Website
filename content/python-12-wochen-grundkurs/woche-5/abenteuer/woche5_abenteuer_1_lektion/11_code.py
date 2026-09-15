# Beispiel 2: Funktion mit bedingtem return
def pruefe_level(level):
    """Prüft, ob ein Charakter für eine Quest bereit ist"""
    if level >= 10:
        return "Bereit für die Quest!"
    else:
        return f"Noch {10 - level} Level needed"

print("=== Level-Prüfung ===")
status1 = pruefe_level(5)
print(f"Level 5: {status1}")

status2 = pruefe_level(12)
print(f"Level 12: {status2}")

status3 = pruefe_level(8)
print(f"Level 8: {status3}")