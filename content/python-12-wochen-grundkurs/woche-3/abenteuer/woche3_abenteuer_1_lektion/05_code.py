# 🔍 Übungen zu Vergleichsoperatoren

# Beispiel 1: = vs == im Vergleich
level = 15  # Zuweisung mit =
if level == 15:  # Vergleich mit ==
    print("✅ Richtig: level ist 15")

# Beispiel 2: Alle vier Vergleichsoperatoren
wert = 10
print(f"Wert: {wert}")
print(f"{wert} < 15: {wert < 15}")
print(f"{wert} <= 10: {wert <= 10}")
print(f"{wert} > 5: {wert > 5}")
print(f"{wert} >= 10: {wert >= 10}")

# Beispiel 3: Praktische Anwendung
gold = 100
kosten = 80
if gold > kosten:
    print(f"🛍️ Kaufen möglich! Übrig: {gold - kosten}")
elif gold == kosten:
    print("💰 Genug für genau einen Kauf!")
else:
    print(f"❌ Zu teuer! Fehlen: {kosten - gold}")