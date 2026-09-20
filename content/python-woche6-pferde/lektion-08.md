# 🚦 Übung 8: break und continue

Manchmal willst du eine Schleife **vorzeitig beenden** oder einen Durchlauf **überspringen**:

```python
pferde = ["Sturmwind", "Blitz", "Luna", "Fuchs", "Balu"]
for eintrag in pferde:
    if eintrag == "Luna":
        print("Gefunden!")
        break                # Schleife sofort beenden
    print(eintrag)

for eintrag in pferde:
    if eintrag == "Blitz":
        continue             # diesen Durchlauf überspringen
    print(eintrag)
```

- **`break`** beendet die Schleife sofort – z. B. sobald du gefunden hast, was du suchst
- **`continue`** überspringt den Rest des aktuellen Durchlaufs und macht mit dem **nächsten** Eintrag weiter

> 💡 Beides steht fast immer in einem `if` innerhalb der Schleife.
