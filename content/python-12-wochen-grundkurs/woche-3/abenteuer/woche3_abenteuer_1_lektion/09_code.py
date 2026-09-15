# Beispiel 1: Level-Bewertung
xp = 750
if xp >= 1000:
    print("🏆 Meister!")
elif xp >= 500:
    print("⭐ Fortgeschritten!")
elif xp >= 100:
    print("🌟 Anfänger!")
else:
    print("📚 Noch viel zu lernen...")

# Beispiel 2: Wetter-Zauber
element = "Wasser"
if element == "Feuer":
    print("🔥 Feuerschlag!")
elif element == "Wasser":
    print("💧 Wasserhose!")
elif element == "Luft":
    print("🌪️ Windstoß!")
elif element == "Erde":
    print("🗿 Erdbeben!")
else:
    print("❓ Unbekanntes Element!")

# Beispiel 3: Heldenklasse
staerke = 8
intelligenz = 12
if staerke > 10 and intelligenz > 10:
    print("⚔️🧠 Paladin!")
elif staerke > 10:
    print("💪 Krieger!")
elif intelligenz > 10:
    print("🧙 Magier!")
else:
    print("👤 Abenteurer!")