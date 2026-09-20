# 📖 Zauberformel 3: Docstrings und gute Namen

Ein guter Magier schreibt seine Zauber ins **Zauberbuch**. In Python heißt das **Docstring**: ein Text in dreifachen Anführungszeichen direkt unter der `def`-Zeile.

```python
def berechne_heilung(basis, multiplikator):
    """Berechnet die Heilungsmenge."""
    return basis * multiplikator

print(berechne_heilung.__doc__)
```

`berechne_heilung.__doc__` (ohne Klammern) zeigt den Docstring an. So verstehen andere – und du selbst in einem Monat – sofort, was die Formel tut.

**Gute Namen:**
- **Kleinbuchstaben mit Unterstrichen:** `berechne_schaden` ✅ – nicht `BerechneSchaden` ❌
- **Ein Verb, das sagt, was passiert:** `berechne_…`, `zeige_…`, `pruefe_…`
- **Sprechend, aber kurz:** `bs` ❌ (unklar), `berechne_das_gesamte_schadensergebnis` ❌ (zu lang)

> 💡 Gleich benannte Parameter helfen genauso: `berechne_schaden(basis, multiplikator)` ist lesbarer als `bs(b, m)`.
