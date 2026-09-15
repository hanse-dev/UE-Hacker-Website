# 🔍 Übungen mit append() und insert()

# Beispiel 1: Elemente hinzufügen
beutesack = []
print(f"Leerer Beutesack: {beutesack}")

# Mit append() am Ende hinzufügen
beutesack.append("Goldring")
print(f"Nach append: {beutesack}")

beutesack.append("Zauberstab")
beutesack.append("Heiltrank")
print(f"Voll gefüllt: {beutesack}")

# Mit insert() an bestimmter Position einfügen
beutesack.insert(0, "Schlüssel")  # Am Anfang
print(f"Nach insert(0): {beutesack}")

beutesack.insert(2, "Amulett")  # An Position 2
print(f"Nach insert(2): {beutesack}")