# Beispiel 3: Futter-Abfrage
print("=== Beispiel 3: Futter-Abfrage ===")
futter = ""
versuche = 0
max_versuche = 3

while futter != "Heu" and versuche < max_versuche:
    futter = input("Was fressen Pferde am liebsten? ")
    versuche += 1
    
    if futter == "Heu":
        print("✅ Richtig!")
    elif versuche >= max_versuche:
        print("❌ Zu viele Versuche! Die Antwort ist: Heu")
    else:
        print(f"Falsch! Noch {max_versuche - versuche} Versuche")