# Beispiel 1: Scan-Ergebnis
signale = 18
if signale >= 15:
    print("⚔️ Lebensformen entdeckt!")
else:
    print("💨 Sektor leer.")

# Beispiel 2: System-Check
druck_ok = False
if druck_ok:
    print("🍺 Druckkammern betriebsbereit.")
else:
    print("🚫 Druckabfall erkannt!")

# Beispiel 3: Energie-Check
energie = 45
verbrauch = 50
if energie >= verbrauch:
    print(f"💰 Sprung möglich! Rest: {energie - verbrauch}%")
else:
    print(f"❌ Sprung unmöglich! Fehlt: {verbrauch - energie}%")