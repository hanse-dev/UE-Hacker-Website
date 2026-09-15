# Beispiel 2: Funktion mit bedingtem return
def pruefe_training_level(erfahrung):
    """Prüft, ob ein Pferd für fortgeschrittenes Training bereit ist"""
    if erfahrung >= 50:
        return "Bereit für fortgeschrittenes Training!"
    else:
        return f"Noch {50 - erfahrung} Trainingseinheiten needed"

print("=== Training-Level-Prüfung ===")
status1 = pruefe_training_level(25)
print(f"Erfahrung 25: {status1}")

status2 = pruefe_training_level(75)
print(f"Erfahrung 75: {status2}")

status3 = pruefe_training_level(40)
print(f"Erfahrung 40: {status3}")