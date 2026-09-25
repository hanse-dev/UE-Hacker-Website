# 🐾 Immer mehr Sonderfälle

Regeln funktionieren super, solange es wenige davon gibt. Aber was, wenn wir ein Tier anhand
seiner Beinanzahl erkennen wollen?

```python
def klassifiziere_tier(beine):
    if beine == 4:
        return "Vierbeiner"
    elif beine == 2:
        return "Zweibeiner"
    elif beine == 6:
        return "Insekt"
    elif beine == 8:
        return "Spinnentier"
    else:
        return "Unbekannt"

print(klassifiziere_tier(4))
print(klassifiziere_tier(8))
```

Läuft gut – aber was passiert bei einer Qualle, die gar keine Beine hat?

```python
print(klassifiziere_tier(0))
```

Ergebnis: `"Unbekannt"`. Unsere Liste an Regeln war einfach nicht vollständig. Stell dir vor, du
willst irgendwann **tausende** Tierarten mit all ihren Ausnahmen unterscheiden – Federn,
Fell, Lebensraum, Größe... Die Liste an `elif`s würde nie enden, und du müsstest für jede neue
Ausnahme von Hand eine neue Zeile schreiben.

> 🤔 Genau dieses Problem – zu viele Regeln für zu viele Sonderfälle – ist einer der Gründe,
> warum es KI überhaupt gibt.
