import random

# Schritt 1 – Turnier initialisieren
def initialisiere_turnier(teilnehmer1, teilnehmer2):
    return {
        "t1": {"name": teilnehmer1["name"], "pferd": teilnehmer1["pferd"], "punkte": 0},
        "t2": {"name": teilnehmer2["name"], "pferd": teilnehmer2["pferd"], "punkte": 0},
        "disziplin": 0
    }

# Schritt 2 – Disziplin ausführen
def fuehre_disziplin_aus(reiter, pferd):
    basis = random.randint(60, 100)
    fehler = random.randint(0, 3)
    return basis, fehler

# Schritt 3 – Punkte berechnen
def berechne_punkte(basis_punkte, fehler_anzahl):
    abzug = fehler_anzahl * 5
    return max(0, basis_punkte - abzug)

# Schritt 4 – Turnier steuern
def starte_turnier(teilnehmer_a, teilnehmer_b, max_disziplinen):
    status = initialisiere_turnier(teilnehmer_a, teilnehmer_b)
    print(f"=== TURNIER: {teilnehmer_a['name']} vs. {teilnehmer_b['name']} ===")
    for i in range(1, max_disziplinen + 1):
        status["disziplin"] = i
        b1, f1 = fuehre_disziplin_aus(status["t1"]["name"], status["t1"]["pferd"])
        b2, f2 = fuehre_disziplin_aus(status["t2"]["name"], status["t2"]["pferd"])
        p1 = berechne_punkte(b1, f1)
        p2 = berechne_punkte(b2, f2)
        status["t1"]["punkte"] += p1
        status["t2"]["punkte"] += p2
        print(f"  Disziplin {i}: {status['t1']['name']} {p1} Pkt | {status['t2']['name']} {p2} Pkt")
    print()
    if status["t1"]["punkte"] >= status["t2"]["punkte"]:
        print(f"Sieger: {teilnehmer_a['name']} ({status['t1']['punkte']} Pkt)")
        print(f"Verlierer: {teilnehmer_b['name']} ({status['t2']['punkte']} Pkt)")
    else:
        print(f"Sieger: {teilnehmer_b['name']} ({status['t2']['punkte']} Pkt)")
        print(f"Verlierer: {teilnehmer_a['name']} ({status['t1']['punkte']} Pkt)")

reiter_a = {"name": "Lena", "pferd": "Sturm"}
reiter_b = {"name": "Max", "pferd": "Luna"}
starte_turnier(reiter_a, reiter_b, 3)