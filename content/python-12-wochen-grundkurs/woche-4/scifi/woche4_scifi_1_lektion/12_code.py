# Beispiel 3: Zugangscodes
print("=== Beispiel 3: Zugangscodes ===")
code = ""
versuche = 0
max_versuche = 3

while code != "NEXUS" and versuche < max_versuche:
    code = input("Gib den Zugangscode ein: ")
    versuche += 1
    
    if code == "NEXUS":
        print("✅ Zugang gewährt!")
    elif versuche >= max_versuche:
        print("❌ Zu viele Versuche! System gesperrt.")
    else:
        print(f"Falsch! Noch {max_versuche - versuche} Versuche")