import random

# Schritt 1 – Kampf initialisieren
def initialisiere_kampf(gruppe1, gruppe2):
    return {
        "gruppe1": {"name": gruppe1["name"], "ruestung": gruppe1["ruestung"], "leben": gruppe1["leben"]},
        "gruppe2": {"name": gruppe2["name"], "ruestung": gruppe2["ruestung"], "leben": gruppe2["leben"]},
        "runde": 0
    }

# Schritt 2 – Schaden berechnen
def berechne_schaden(basis_schaden, ruestung_staerke):
    schaden = basis_schaden - ruestung_staerke / 10
    return max(1, int(schaden))

# Schritt 3 – Kampfrunde ausführen
def fuehre_runde_aus(status):
    status["runde"] += 1
    angreifer, verteidiger = ("gruppe1", "gruppe2") if random.random() < 0.5 else ("gruppe2", "gruppe1")
    basis = random.randint(15, 35)
    schaden = berechne_schaden(basis, status[verteidiger]["ruestung"])
    status[verteidiger]["leben"] -= schaden
    print(f"  Runde {status['runde']}: {status[angreifer]['name']} greift an – {schaden} Schaden!")
    print(f"  {status[verteidiger]['name']} hat noch {max(0, status[verteidiger]['leben'])} LP")

# Schritt 4 – Kampf steuern
def starte_kampf(gruppe_a, gruppe_b, max_runden):
    status = initialisiere_kampf(gruppe_a, gruppe_b)
    print(f"=== KAMPF: {gruppe_a['name']} vs. {gruppe_b['name']} ===")
    for _ in range(max_runden):
        fuehre_runde_aus(status)
        if status["gruppe1"]["leben"] <= 0 or status["gruppe2"]["leben"] <= 0:
            break
    print()
    if status["gruppe1"]["leben"] > status["gruppe2"]["leben"]:
        print(f"Sieger: {gruppe_a['name']} ({status['gruppe1']['leben']} LP übrig)")
        print(f"Verlierer: {gruppe_b['name']}")
    else:
        print(f"Sieger: {gruppe_b['name']} ({status['gruppe2']['leben']} LP übrig)")
        print(f"Verlierer: {gruppe_a['name']}")

helden = {"name": "Lichtwächter", "ruestung": 50, "leben": 200}
monster = {"name": "Schattendrache", "ruestung": 30, "leben": 180}
starte_kampf(helden, monster, 10)