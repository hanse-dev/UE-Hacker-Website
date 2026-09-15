import random

# Schritt 1 – Kampf initialisieren
def initialisiere_kampf(flotte1, flotte2):
    return {
        "f1": {"name": flotte1["name"], "schild": flotte1["schild"], "huelle": flotte1["huelle"]},
        "f2": {"name": flotte2["name"], "schild": flotte2["schild"], "huelle": flotte2["huelle"]},
        "runde": 0
    }

# Schritt 2 – Schaden berechnen
def berechne_schaden(basis_schaden, schild_staerke):
    schaden = basis_schaden - schild_staerke / 10
    return max(1, int(schaden))

# Schritt 3 – Kampfrunde ausführen
def fuehre_runde_aus(status):
    status["runde"] += 1
    angreifer, ziel = ("f1", "f2") if random.random() < 0.5 else ("f2", "f1")
    basis = random.randint(20, 50)
    # Bonus: Spezialwaffe mit 20% Wahrscheinlichkeit
    if random.random() < 0.2:
        basis *= 2
        print(f"  *** SPEZIALWAFFE! ***")
    schaden = berechne_schaden(basis, status[ziel]["schild"])
    status[ziel]["huelle"] -= schaden
    print(f"  Runde {status['runde']}: {status[angreifer]['name']} feuert – {schaden} Schaden!")
    print(f"  {status[ziel]['name']} Hülle: {max(0, status[ziel]['huelle'])}")

# Schritt 4 – Kampf steuern
def starte_simulation(flotte1, flotte2, max_runden):
    status = initialisiere_kampf(flotte1, flotte2)
    print(f"=== KAMPFSIMULATION: {flotte1['name']} vs. {flotte2['name']} ===")
    for _ in range(max_runden):
        fuehre_runde_aus(status)
        if status["f1"]["huelle"] <= 0 or status["f2"]["huelle"] <= 0:
            break
    print()
    if status["f1"]["huelle"] > status["f2"]["huelle"]:
        print(f"Sieger: {flotte1['name']} (Hülle: {status['f1']['huelle']})")
        print(f"Verlierer: {flotte2['name']}")
    else:
        print(f"Sieger: {flotte2['name']} (Hülle: {status['f2']['huelle']})")
        print(f"Verlierer: {flotte1['name']}")

alpha = {"name": "Alpha-Flotte", "schild": 40, "huelle": 300}
beta = {"name": "Beta-Flotte", "schild": 60, "huelle": 250}
starte_simulation(alpha, beta, 8)