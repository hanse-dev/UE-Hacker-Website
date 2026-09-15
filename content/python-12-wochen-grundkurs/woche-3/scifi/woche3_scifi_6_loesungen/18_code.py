# Schritt 1 – Quiz-Antworten (True = richtig, False = falsch)
antwort1 = True   # Frage 1: KI lernt aus Daten – Richtig
antwort2 = True   # Frage 2: Python ist eine Programmiersprache – Richtig
antwort3 = False  # Frage 3: KI kann alles denken wie Menschen – Falsch
antwort4 = True   # Frage 4: Algorithmen sind Schritt-für-Schritt-Anleitungen – Richtig
antwort5 = True   # Frage 5: Daten sind wichtig für KI – Richtig

# Schritt 2 & 3 – Prüfung und Punkte zählen
punkte = 0

print("=== KI-QUIZ AUSWERTUNG ===")
if antwort1:
    print("Frage 1: ✅ Richtig! +100 Punkte")
    punkte += 100
else:
    print("Frage 1: ❌ Falsch!")

if antwort2:
    print("Frage 2: ✅ Richtig! +100 Punkte")
    punkte += 100
else:
    print("Frage 2: ❌ Falsch!")

if antwort3:
    print("Frage 3: ✅ Richtig! +100 Punkte")
    punkte += 100
else:
    print("Frage 3: ❌ Falsch!")

if antwort4:
    print("Frage 4: ✅ Richtig! +100 Punkte")
    punkte += 100
else:
    print("Frage 4: ❌ Falsch!")

if antwort5:
    print("Frage 5: ✅ Richtig! +100 Punkte")
    punkte += 100
else:
    print("Frage 5: ❌ Falsch!")

print()
print(f"Gesamtpunkte: {punkte} / 500")

# Schritt 4 – Abschlussbewertung
if punkte >= 400:
    note = "A"
elif punkte >= 300:
    note = "B"
elif punkte >= 200:
    note = "C"
else:
    note = "D"
print(f"Note: {note}")

# Schritt 5 – Zertifikat
if punkte >= 300:
    print()
    print("🎖️ === DIGITALES KI-ZERTIFIKAT ===")
    print("Hiermit wird zertifiziert, dass dieser Crew-Member")
    print("das KI-Quiz erfolgreich bestanden hat!")
    print(f"Punktzahl: {punkte} | Note: {note}")
    print("Ausgestellt durch: Galaktisches Institut für KI")
else:
    print("Leider nicht bestanden. Weiteres Studium erforderlich!")