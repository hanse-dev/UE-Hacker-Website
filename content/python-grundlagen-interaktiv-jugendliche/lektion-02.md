# Variablen

Variablen speichern Werte unter einem Namen. Du kannst sie jederzeit überschreiben – der alte Wert geht dabei verloren.

```python
username = "alex"
score = 1500
print(username)
print(score)
```

Das `=` ist hier keine mathematische Gleichheit, sondern eine **Zuweisung**: "Speichere den Wert rechts unter dem Namen links." Weist du derselben Variable später einen neuen Wert zu, wird der alte einfach ersetzt:

```python
score = 1500
score = 1800  # überschreibt den alten Wert
print(score)  # gibt 1800 aus
```

Du kannst auch eine Variable auf Basis ihres eigenen Werts aktualisieren:

```python
score = 1500
score = score + 100
print(score)  # gibt 1600 aus
```

**Variablennamen:** Kleinbuchstaben, Unterstriche statt Leerzeichen (`mein_name` statt `mein name`), keine Zahlen am Anfang, keine reservierten Wörter wie `print` oder `if`. Sinnvolle Namen (`follower_anzahl` statt `x`) machen deinen Code später deutlich leichter lesbar – für andere und für dich selbst.
