# Beispiel 1: Verschiedene Variablentypen
held_name = "Aragorn"      # Text (String)
held_level = 1             # Zahl (Integer)
held_gold = 50             # Zahl (Integer)

# Beispiel 2: Variablen ausgeben
print("Helden-Name:")
print(held_name)
print("Level:")
print(held_level)
print("Gold:")
print(held_gold)

# Beispiel 3: Variablen können sich ändern
print("Gold vor dem Kampf: " + str(held_gold))
held_gold = 150  # Neuer Wert
print("Gold nach dem Sieg: " + str(held_gold))