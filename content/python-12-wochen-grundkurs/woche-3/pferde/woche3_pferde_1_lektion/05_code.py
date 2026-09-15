# 🔍 Übungen zu Vergleichsoperatoren

# Beispiel 1: = vs == im Vergleich
alter = 8  # Zuweisung mit =
if alter == 8:  # Vergleich mit ==
    print("✅ Richtig: Das Pferd ist 8 Jahre alt")

# Beispiel 2: Alle vier Vergleichsoperatoren
groesse = 160  # cm Stockmaß
print(f"Stockmaß: {groesse} cm")
print(f"{groesse} < 165: {groesse < 165}")
print(f"{groesse} <= 160: {groesse <= 160}")
print(f"{groesse} > 150: {groesse > 150}")
print(f"{groesse} >= 160: {groesse >= 160}")

# Beispiel 3: Praktische Anwendung
futter = 25
bedarf = 20
if futter > bedarf:
    print(f"🌾 Genug Futter! Übrig: {futter - bedarf} kg")
elif futter == bedarf:
    print("⚖️ Perfekte Menge!")
else:
    print(f"❌ Zu wenig Futter! Fehlen: {bedarf - futter} kg")