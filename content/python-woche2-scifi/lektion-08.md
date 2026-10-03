# 📟 Systemprotokoll 8: Eingaben verarbeiten

Du kennst `input()` aus Woche 1: Die **Funktion** gibt dir die Antwort der Crew zurück – **immer als Text (`str`)**, auch wenn eine Zahl getippt wird! Willst du damit rechnen, musst du sie umwandeln:

```python
eingabe = input("Energie-Level? ")    # Text, z.B. "70"
energie = int(eingabe)                # jetzt eine Zahl: 70
print(f"Nach dem Aufladen: {energie + 10}%")
```

Für Kommazahlen nimmst du `float()` statt `int()`.

> 💡 Tippe im Eingabefenster nur eine **ganze Zahl** ein – sonst kann `int()` sie nicht umwandeln.
