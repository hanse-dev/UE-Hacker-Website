# Schritt 1 – Schätze erfassen
truhe1_name = "Rubintruhe"
truhe1_gold = 320
truhe2_name = "Smaragdtruhe"
truhe2_gold = 480
truhe3_name = "Saphirtruhe"
truhe3_gold = 210
truhe4_name = "Diamanttruhe"
truhe4_gold = 750
truhe5_name = "Goldtruhe"
truhe5_gold = 390
truhe6_name = "Silbertruhe"
truhe6_gold = 160
truhe7_name = "Amethysttruhe"
truhe7_gold = 290
truhe8_name = "Topastruhe"
truhe8_gold = 440

# Schritt 2 – Schatzprotokoll erstellen
print("=== SCHATZRAUM-PROTOKOLL ===")
print(f"{truhe1_name}: {truhe1_gold} Gold")
print(f"{truhe2_name}: {truhe2_gold} Gold")
print(f"{truhe3_name}: {truhe3_gold} Gold")
print(f"{truhe4_name}: {truhe4_gold} Gold")
print(f"{truhe5_name}: {truhe5_gold} Gold")
print(f"{truhe6_name}: {truhe6_gold} Gold")
print(f"{truhe7_name}: {truhe7_gold} Gold")
print(f"{truhe8_name}: {truhe8_gold} Gold")
print()

# Schritt 3 – Durchschnitt berechnen
gesamtwert = truhe1_gold + truhe2_gold + truhe3_gold + truhe4_gold + truhe5_gold + truhe6_gold + truhe7_gold + truhe8_gold
durchschnitt = gesamtwert / 8
print(f"Durchschnittswert: {durchschnitt} Gold")

# Schritt 4 – Reichste Truhe finden
hoechster_wert = truhe4_gold
reichste_truhe = truhe4_name
print(f"Reichste Truhe: {reichste_truhe} mit {hoechster_wert} Gold")

# Schritt 5 – Gesamtwert
print(f"Gesamtwert aller Truhen: {gesamtwert} Gold")

# Bonus: Truhen unter Durchschnitt
unter_durchschnitt = 0
if truhe1_gold < durchschnitt:
    unter_durchschnitt += 1
if truhe2_gold < durchschnitt:
    unter_durchschnitt += 1
if truhe3_gold < durchschnitt:
    unter_durchschnitt += 1
if truhe4_gold < durchschnitt:
    unter_durchschnitt += 1
if truhe5_gold < durchschnitt:
    unter_durchschnitt += 1
if truhe6_gold < durchschnitt:
    unter_durchschnitt += 1
if truhe7_gold < durchschnitt:
    unter_durchschnitt += 1
if truhe8_gold < durchschnitt:
    unter_durchschnitt += 1
print(f"Truhen unter dem Durchschnitt: {unter_durchschnitt}")
