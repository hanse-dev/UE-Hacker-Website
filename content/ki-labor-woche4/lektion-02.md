# 📊 Genauigkeit berechnen

Wenn du eine Vorhersage mit dem bekannten, richtigen Wert vergleichst, ist das entweder
**richtig** oder **falsch**. Zählst du das über mehrere Vorhersagen zusammen, bekommst du die
**Genauigkeit** (englisch: *accuracy*) – den Anteil der richtigen Vorhersagen in Prozent.

```python
def ist_richtig(vorhersage, erwartet):
    return vorhersage == erwartet

def genauigkeit(vorhersagen, erwartete_werte):
    richtig = 0
    for i in range(len(vorhersagen)):
        if ist_richtig(vorhersagen[i], erwartete_werte[i]):
            richtig += 1
    return round(richtig / len(vorhersagen) * 100)

vorhersagen = ["Saeugetier", "Vogel", "Insekt", "Vogel"]
erwartete_werte = ["Saeugetier", "Vogel", "Vogel", "Vogel"]

print(genauigkeit(vorhersagen, erwartete_werte))
```

`round()` rundet das Ergebnis auf eine ganze Zahl, damit du z.B. `75` statt `75.0` bekommst.
