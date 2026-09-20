# 🚦 Sammlungs-Zauber 8: break und continue

Manchmal willst du eine Schleife **vorzeitig beenden** oder einen Durchlauf **überspringen**:

```python
schaetze = ["Gold", "Kristall", "Amulett", "Krone", "Ring"]
for eintrag in schaetze:
    if eintrag == "Amulett":
        print("Gefunden!")
        break                # Schleife sofort beenden
    print(eintrag)

for eintrag in schaetze:
    if eintrag == "Kristall":
        continue             # diesen Durchlauf überspringen
    print(eintrag)
```

- **`break`** beendet die Schleife sofort – z. B. sobald du gefunden hast, was du suchst
- **`continue`** überspringt den Rest des aktuellen Durchlaufs und macht mit dem **nächsten** Eintrag weiter

> 💡 Beides steht fast immer in einem `if` innerhalb der Schleife.
