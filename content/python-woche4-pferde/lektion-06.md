## 💪 Übung 6: Training bis zur Erschöpfung

Die Bedingung einer while-Schleife kann jeden Vergleich enthalten. Dann läuft die Schleife so lange, bis sich ein Wert ändert:

```python
ausdauer = 100
runde = 1

while ausdauer > 20:
    ausdauer -= 15
    print(f"Runde {runde}: übrig {ausdauer}%")
    runde += 1

print(f"Training beendet nach {runde-1} Runden!")
```

Bei jedem Durchlauf sinkt die Ausdauer um 15. Sobald sie **nicht mehr über 20** liegt, endet die Schleife.

> 🐴 **Merke:** Die Variable in der Bedingung (`ausdauer`) muss sich **im Schleifenkörper ändern** – sonst gibt es eine Endlosschleife.
