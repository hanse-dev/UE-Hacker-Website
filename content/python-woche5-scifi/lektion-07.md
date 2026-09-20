# 📖 Systemprotokoll 7: Docstrings und gute Namen

Jedes gute Protokoll hat ein **Handbuch**. In Python heißt das **Docstring**: ein Text in dreifachen Anführungszeichen direkt unter der `def`-Zeile.

```python
def berechne_treibstoff(distanz):
    """Berechnet den Treibstoffbedarf."""
    return distanz * 3

print(berechne_treibstoff.__doc__)
```

`berechne_treibstoff.__doc__` (ohne Klammern) zeigt den Docstring an. So verstehen andere – und du selbst in einem Monat – sofort, was das Protokoll tut.

**Gute Namen:**
- **Kleinbuchstaben mit Unterstrichen:** `berechne_treibstoff` ✅ – nicht `BerechneTreibstoff` ❌
- **Ein Verb, das sagt, was passiert:** `berechne_…`, `zeige_…`, `pruefe_…`
- **Sprechend, aber kurz:** `bt` ❌ (unklar), `berechne_den_gesamten_treibstoffbedarf_der_mission` ❌ (zu lang)

> 💡 Gut benannte Parameter helfen genauso: `berechne_frachtraum(laenge, breite)` ist lesbarer als `fr(l, b)`.
