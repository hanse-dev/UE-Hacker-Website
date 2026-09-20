# 📖 Übung 7: Docstrings und gute Namen

Ein guter Reiter führt ein **Trainingsbuch**. In Python heißt das **Docstring**: ein Text in dreifachen Anführungszeichen direkt unter der `def`-Zeile.

```python
def berechne_futter(pferde):
    """Berechnet die Futtermenge pro Tag."""
    return pferde * 8

print(berechne_futter.__doc__)
```

`berechne_futter.__doc__` (ohne Klammern) zeigt den Docstring an. So verstehen andere – und du selbst in einem Monat – sofort, was die Routine tut.

**Gute Namen:**
- **Kleinbuchstaben mit Unterstrichen:** `berechne_futter` ✅ – nicht `BerechneFutter` ❌
- **Ein Verb, das sagt, was passiert:** `berechne_…`, `zeige_…`, `pruefe_…`
- **Sprechend, aber kurz:** `bf` ❌ (unklar), `berechne_die_gesamte_futtermenge_pro_tag` ❌ (zu lang)

> 💡 Gut benannte Parameter helfen genauso: `berechne_flaeche(laenge, breite)` ist lesbarer als `fl(l, b)`.
