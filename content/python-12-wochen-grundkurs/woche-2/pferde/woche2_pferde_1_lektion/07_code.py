# Beispiel 1: Mathematische Operationen
pferde_a = 12
pferde_b = 8
print(f"Gesamte Pferde: {pferde_a + pferde_b}")
print(f"Unterschied: {pferde_a - pferde_b}")
print(f"Doppelte Ställe: {pferde_a * 2}")
print(f"Pferde pro Box: {pferde_a / 4}")

# Beispiel 2: String-Operationen
name = "Sternen"
zusatz = "prinz"
voll_name = name + zusatz
print(f"Voller Name: {voll_name}")
print(f"Wiehern: {name * 3}")

# Beispiel 3: Typumwandlung
alter_text = "5"
alter_zahl = int(alter_text)
print(f"Alter als Text: {alter_text} (Typ: {type(alter_text)})")
print(f"Alter als Zahl: {alter_zahl} (Typ: {type(alter_zahl)})")

# Beispiel 4: Eingaben verarbeiten
# Eingabe simuliert (später mit input())
eingabe = "15"
zahl = int(eingabe)
print(f"{zahl} kg Heu für {zahl * 2} Tage reichen.")