# Schritt 1 – Zwei 🔥 Feuersteine verschmelzen
vorname = "Luna"
nachname = "Silbermond"
name = f"{vorname} {nachname}"
print(f"Verschmolzener Name: {name}")

# Schritt 2 – Zwei 🪨 Erdsteine verschmelzen
gold_a = 150
gold_b = 75
gold_summe = gold_a + gold_b
print(f"Verschmolzenes Gold: {gold_summe}")

# Schritt 3 – Zwei 💧 Wassersteine verschmelzen
schaden_a = 23.5
schaden_b = 31.0
schaden_durchschnitt = (schaden_a + schaden_b) / 2
print(f"Durchschnittsschaden: {schaden_durchschnitt}")

# Schritt 4 – 🔥 Feuer und 🪨 Erde verschmelzen
held = "Thorin"
level = 12
nachricht = held + " ist Level " + str(level)
print(f"Verschmolzene Nachricht: {nachricht}")

# Bonus: ohne str() würde Python einen TypeError werfen:
# TypeError: can only concatenate str (not "int") to str
