# Beispiel 3: Benutzereingabe validieren
print("=== Beispiel 3: Passwort-Abfrage ===")
passwort = ""
versuche = 0
max_versuche = 3

while passwort != "Geheim" and versuche < max_versuche:
    passwort = input("Gib das Passwort ein: ")
    versuche += 1
    
    if passwort == "Geheim":
        print("✅ Zugang gewährt!")
    elif versuche >= max_versuche:
        print("❌ Zu viele Versuche!")
    else:
        print(f"Falsch! Noch {max_versuche - versuche} Versuche")