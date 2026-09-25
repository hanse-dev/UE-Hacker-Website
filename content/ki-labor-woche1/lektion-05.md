# ⚠️ Was KI (noch) nicht kann

Ein Modell ist immer nur so gut wie seine Trainingsdaten. Mit nur zwei Beispielen kann es fast
nichts Neues richtig einschätzen:

```python
kleines_modell = {"hund": "Tier", "katze": "Tier"}

def vorhersage_sicherheit(modell, eingabe):
    if eingabe in modell:
        return f"Sicher: {modell[eingabe]}"
    else:
        return "Unsicher: unbekannt"

print(vorhersage_sicherheit(kleines_modell, "hund"))
print(vorhersage_sicherheit(kleines_modell, "vogel"))
```

`"vogel"` steckt einfach nicht in den Trainingsdaten – das Modell hat also keine Ahnung. Das ist
kein Sonderfall, sondern eine **grundsätzliche Grenze**: Eine KI kann nur Muster in den Daten
finden, die sie tatsächlich gesehen hat. Drei wichtige Konsequenzen, die dich diesen Kurs über
begleiten:

- **Wenige/einseitige Beispiele → schlechte Vorhersagen.** Fehlen bestimmte Fälle komplett in den
  Trainingsdaten, kann das Modell sie nicht erkennen.
- **Schiefe Trainingsdaten → unfaire Vorhersagen.** Wenn die Beispiele selbst schon einseitig
  sind, übernimmt das Modell diese Schieflage (dazu mehr in Woche 8).
- **KI "versteht" nichts.** Sie erkennt Muster in Daten – sie weiß nicht, *warum* ein Muster
  gilt.
