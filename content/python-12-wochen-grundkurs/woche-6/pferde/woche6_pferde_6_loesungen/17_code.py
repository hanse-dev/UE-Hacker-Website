def generiere_training(pferdetyp, schwierigkeit):
    basis = ["Aufwärmen", "Schritt", "Trab"]
    mittel = ["Galopp", "Dressur", "Hindernisse"]
    profi = ["Springen", "Voltigieren", "Pirouette"]
    training = list(basis)
    if schwierigkeit >= 2:
        training += mittel
    if schwierigkeit >= 3:
        training += profi
    return [f"{pferdetyp}-{t}" for t in training]

plan_a = generiere_training("Warmblut", 2)
plan_b = generiere_training("Pony", 3)
print(f"Warmblut-Plan: {plan_a}")
print(f"Pony-Plan: {plan_b}")

# Filtern: nur Einheiten mit "D"
dressur = [t for t in plan_b if "Dressur" in t or "Pirouette" in t]
print(f"Dressur-Einheiten: {dressur}")