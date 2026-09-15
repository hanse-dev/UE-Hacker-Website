# 🔍 Übungen mit append() und insert()

# Beispiel 1: Elemente hinzufügen
trainings_plan = []
print(f"Leerer Trainingsplan: {trainings_plan}")

# Mit append() am Ende hinzufügen
trainings_plan.append("Longieren")
print(f"Nach append: {trainings_plan}")

trainings_plan.append("Dressur")
trainings_plan.append("Springen")
print(f"Voll gefüllt: {trainings_plan}")

# Mit insert() an bestimmter Position einfügen
trainings_plan.insert(0, "Aufwärmen")  # Am Anfang
print(f"Nach insert(0): {trainings_plan}")

trainings_plan.insert(2, "Cavaletti")  # An Position 2
print(f"Nach insert(2): {trainings_plan}")