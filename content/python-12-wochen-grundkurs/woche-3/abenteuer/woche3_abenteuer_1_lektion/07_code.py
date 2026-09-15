# Beispiel 1: Erfolg oder Misserfolg
wurf = 18
if wurf >= 15:
    print("⚔️ Kritischer Treffer!")
else:
    print("💨 Normaler Schlag")

# Beispiel 2: Altersprüfung
alter = 17
if alter >= 18:
    print("🍺 Du darfst betreten.")
else:
    print("🚫 Zu jung für diese Taverne.")

# Beispiel 3: Inventar-Check
gold = 45
kosten = 50
if gold >= kosten:
    print(f"💰 Kauf erfolgreich! Rest: {gold - kosten}")
else:
    print(f"❌ Nicht genug Gold! Fehlt: {kosten - gold}")