# 🎤 Übung 9: Eingaben verarbeiten

Du kennst `input()` aus Woche 1: Die **Funktion** gibt dir die Antwort des Benutzers zurück – **immer als Text (`str`)**, auch wenn er eine Zahl tippt! Willst du damit rechnen, musst du sie umwandeln:

```python
eingabe = input("Wie viele kg Heu? ")   # Text, z.B. "15"
zahl = int(eingabe)                     # jetzt eine Zahl: 15
print(f"{zahl} kg Heu für {zahl * 2} Tage reichen.")
```

> 💡 Tippe im Eingabefenster nur eine **ganze Zahl** ein – sonst kann `int()` sie nicht umwandeln.
