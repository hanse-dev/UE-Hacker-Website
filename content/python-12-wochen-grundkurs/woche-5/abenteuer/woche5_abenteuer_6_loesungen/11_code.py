import random

# Schritt 1 – Begrüßungszauber
def begruesse_magier():
    print("Sei gegrüßt, Magierlehrling!")
    print("Willkommen in der Schule der Zauberformeln!")

begruesse_magier()
begruesse_magier()

# Schritt 2 – Mana-Berechnung
def berechne_mana(level, basis_mana):
    return level * basis_mana

# Schritt 3 – Zauber-Verfügbarkeit
def ist_zauber_moeglich(mana_kosten, aktuelles_mana):
    return aktuelles_mana >= mana_kosten

# Schritt 4 – Haupt-Block
mana = berechne_mana(5, 20)
print(f"Mana: {mana}")

if ist_zauber_moeglich(80, mana):
    print("Feuerball ist möglich!")
else:
    print("Nicht genug Mana für Feuerball.")

if ist_zauber_moeglich(120, mana):
    print("Blitzsturm ist möglich!")
else:
    print("Nicht genug Mana für Blitzsturm.")

# Bonus – zufälliger Zauber
def generiere_zauber():
    zauber = ["Feuerball", "Heilung", "Schild", "Blitz", "Eisnova"]
    return random.choice(zauber)

print(f"Zufälliger Zauber: {generiere_zauber()}")