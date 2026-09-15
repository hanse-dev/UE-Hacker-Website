# Beispiel 1: Rang-Bewertung
punkte = 750
if punkte >= 1000:
    print("🏆 Fleet-Kommandant!")
elif punkte >= 500:
    print("⭐ Kapitän!")
elif punkte >= 100:
    print("🌟 Leutnant!")
else:
    print("📚 Kadett!")

# Beispiel 2: Waffensystem
waffe = "Laser"
if waffe == "Laser":
    print("🔥 Laser aktiviert!")
elif waffe == "Plasma":
    print("💧 Plasmathron geladen!")
elif waffe == "Quantum":
    print("🌪️ Quantum-Torpedo bereit!")
elif waffe == "Ion":
    print("⚡ Ionengeschütz online!")
else:
    print("❓ Unbekannte Waffe!")

# Beispiel 3: Schiffs-Klasse
schild = 8
waffen = 12
if schild > 10 and waffen > 10:
    print("⚔️🧠 Schlachtschiff!")
elif schild > 10:
    print("💪 Kreuzer!")
elif waffen > 10:
    print("🧙 Zerstörer!")
else:
    print("👤 Fregatte!")