# Beispiel 2: Funktion mit bedingtem return
def pruefe_system_status(energie_level):
    """Prüft, ob das System für eine Mission bereit ist"""
    if energie_level >= 75:
        return "System bereit für Mission!"
    else:
        return f"Noch {75 - energie_level}% Energie needed"

print("=== System-Status-Prüfung ===")
status1 = pruefe_system_status(60)
print(f"Energie 60%: {status1}")

status2 = pruefe_system_status(90)
print(f"Energie 90%: {status2}")

status3 = pruefe_system_status(70)
print(f"Energie 70%: {status3}")