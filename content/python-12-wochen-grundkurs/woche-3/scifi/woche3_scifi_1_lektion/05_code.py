# 🔍 Übungen zu Vergleichsoperatoren

# Beispiel 1: = vs == im Vergleich
rang = 15  # Zuweisung mit =
if rang == 15:  # Vergleich mit ==
    print("✅ Richtig: Rang 15 erreicht")

# Beispiel 2: Alle vier Vergleichsoperatoren
wert = 42
print(f"Wert: {wert}")
print(f"{wert} < 50: {wert < 50}")
print(f"{wert} <= 42: {wert <= 42}")
print(f"{wert} > 30: {wert > 30}")
print(f"{wert} >= 42: {wert >= 42}")

# Beispiel 3: Praktische Anwendung
energie = 85
verbrauch = 60
if energie > verbrauch:
    print(f"⚡ Sprung möglich! Übrig: {energie - verbrauch}%")
elif energie == verbrauch:
    print("⚖️ Genau für einen Sprung!")
else:
    print(f"❌ Sprung unmöglich! Fehlen: {verbrauch - energie}%")