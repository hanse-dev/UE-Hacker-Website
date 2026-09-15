# Schritt 1 – Kämpferdaten
level = 48
siege = 42
niederlagen = 8

# Schritt 2 – Siegquote berechnen
gesamt_kaempfe = siege + niederlagen
siegquote = siege / gesamt_kaempfe
print(f"Kämpfer: Level {level}, Siege: {siege}, Niederlagen: {niederlagen}")
print(f"Siegquote: {siegquote:.0%}")

# Schritt 3 – Legendär-Status
if level >= 50 and siegquote > 0.8:
    print("🏆 LEGENDÄR! Du bist eine Legende der Arena!")
elif level >= 30 and siegquote > 0.6:
    print("⭐ MEISTER! Respektabler Kämpfer!")
elif level >= 10:
    print("🗡️ KRIEGER – Weiter trainieren!")
else:
    print("🌱 LEHRLING – Der Weg ist noch lang.")

# Schritt 5 – Perfekte-Serie-Bonus
if niederlagen == 0:
    print("+100 Bonus für perfekte Serie!")