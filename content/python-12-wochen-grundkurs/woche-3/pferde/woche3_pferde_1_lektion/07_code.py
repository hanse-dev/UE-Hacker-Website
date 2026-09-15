# Beispiel 1: Hürdensprung
hoehe = 120
if hoehe <= 100:
    print("⚔️ Leichte Hürde gemeistert!")
else:
    print("💨 Anspruchsvolle Hürde!")

# Beispiel 2: Wetterprüfung
regnet = False
if regnet:
    print("🌧️ Wir reiten in der Halle.")
else:
    print("☀️ Perfekt für die Weide!")

# Beispiel 3: Futter-Check
heu_vorrat = 45
bedarf = 50
if heu_vorrat >= bedarf:
    print(f"💰 Genug Heu! Rest: {heu_vorrat - bedarf} kg")
else:
    print(f"❌ Zu wenig Heu! Fehlt: {bedarf - heu_vorrat} kg")