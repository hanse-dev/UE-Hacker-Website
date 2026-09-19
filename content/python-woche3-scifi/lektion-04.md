# 📟 Systemprotokoll 4: if-elif-else

Manchmal gibt es **mehr als zwei** Möglichkeiten. Dafür gibt es `elif` (kurz für „else if“):

```python
punkte = 750
if punkte >= 1000:
    print("Fleet-Kommandant!")
elif punkte >= 500:
    print("Kapitän!")
elif punkte >= 100:
    print("Leutnant!")
else:
    print("Kadett!")
```

- Python prüft die Bedingungen **von oben nach unten**.
- **Nur der erste wahre Pfad** wird ausgeführt, danach wird der Rest übersprungen.
- `elif` braucht **immer eine Bedingung** (im Gegensatz zu `else`).
- Du darfst beliebig viele `elif` nutzen; `else` am Ende ist optional und fängt alles andere ab.

Auch Text lässt sich so auswählen:

```python
waffe = "Laser"
if waffe == "Laser":
    print("Laser aktiviert!")
elif waffe == "Plasma":
    print("Plasmakanone geladen!")
else:
    print("Unbekannte Waffe!")
```

> 📡 **Merke:** Die Reihenfolge zählt! Prüfe die strengste Bedingung zuerst.
