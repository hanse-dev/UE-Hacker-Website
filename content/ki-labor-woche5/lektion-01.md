# 🌳 Was ist ein Entscheidungsbaum?

Ein **Entscheidungsbaum** trifft eine Vorhersage, indem er eine oder mehrere Ja/Nein-Fragen zu
den Merkmalen eines Beispiels stellt – ganz ähnlich wie ein `if`/`else` in Python. Bei einem
Merkmal mit Zahlenwerten ist die Frage meist ein Vergleich mit einem **Schwellenwert**: "Ist der
Wert kleiner als X?"

Ein Beispiel: Soll ich einen Regenschirm mitnehmen? Wenn die Regenwahrscheinlichkeit hoch genug
ist, ja – sonst nein. Als Python-Funktion:

```python
def schirm_mitnehmen(regen_prozent):
    if regen_prozent >= 50:
        return "ja"
    else:
        return "nein"

print(schirm_mitnehmen(80))
print(schirm_mitnehmen(20))
```

Diese Funktion **ist** bereits ein winziger Entscheidungsbaum: eine Frage (`regen_prozent >= 50`)
und zwei mögliche Antworten ("ja"/"nein"). In den nächsten Lektionen lernst du, wie ein Programm
so einen Schwellenwert **selbst aus Daten** findet, statt dass du ihn von Hand festlegst.
