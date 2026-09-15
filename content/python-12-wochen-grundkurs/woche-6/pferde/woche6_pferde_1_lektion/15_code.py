pferde = ["Thunder", "Luna", "Storm", "Shadow", "Bella"]

# break: Suche beenden sobald das gesuchte Pferd gefunden ist
print("=== Pferde-Suche ===")
for pferd in pferde:
    print(f"Prüfe: {pferd}")
    if pferd == "Storm":
        print("🐎 Storm gefunden! Suche beendet.")
        break

# continue: kranke Pferde beim Training überspringen
print("\n=== Trainingsplan ohne kranke Pferde ===")
kranke_pferde = ["Luna"]
for pferd in pferde:
    if pferd in kranke_pferde:
        continue
    print(f"  - {pferd} wird trainiert")