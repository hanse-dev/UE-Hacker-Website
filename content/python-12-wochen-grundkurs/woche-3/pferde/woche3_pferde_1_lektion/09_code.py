# Beispiel 1: Reitfertigkeit
erfahrung = 750
if erfahrung >= 1000:
    print("🏆 Meisterreiter!")
elif erfahrung >= 500:
    print("⭐ Fortgeschrittener Reiter!")
elif erfahrung >= 100:
    print("🌟 Anfänger!")
else:
    print("📚 Noch viel zu üben...")

# Beispiel 2: Pferdedisziplin
disziplin = "Springen"
if disziplin == "Dressur":
    print("🎆 Elegante Dressur!")
elif disziplin == "Springen":
    print("🏇 Sprungkurs!")
elif disziplin == "Western":
    print("🤠 Western-Style!")
elif disziplin == "Voltigieren":
    print("🤸 Voltigier-Akrobatik!")
else:
    print("❓ Unbekannte Disziplin!")

# Beispiel 3: Pferde-Typ
groesse = 168
temperament = 8
if groesse > 170 and temperament > 7:
    print("⚔️🧠 Warmblut für Sport!")
elif groesse > 170:
    print("💪 Kaltblut für Arbeit!")
elif temperament > 7:
    print("🐎 Vollblut für Rennen!")
else:
    print("👤 Pony für Freizeit!")