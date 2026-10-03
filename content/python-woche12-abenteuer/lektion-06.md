# ⚔️ Etappe 6: Falsche Eingaben abfangen

*Wissen aus Woche 8: try/except*

Spieler tippen manchmal Unsinn. Ein Befehl wie `gehe norden` besteht aus zwei Wörtern, die `split()` in `aktion` und `ziel` zerlegt. Bei `hallo` passt die Anzahl nicht, und Python wirft einen `ValueError`. `try/except` fängt ihn ab:

```python
def fuehre_aus(spieler, text):
    try:
        aktion, ziel = text.split()
    except ValueError:
        print("🤔 Ich verstehe nur Befehle aus zwei Wörtern, z.B. 'gehe norden' oder 'nimm Fackel'.")
        return
    if aktion == "gehe":
        spieler.gehe(ziel)
        pruefe_gegner(spieler)
    elif aktion == "nimm":
        spieler.nimm(ziel)
    else:
        print(f"🤔 '{aktion}' kenne ich nicht. Versuche 'gehe' oder 'nimm'.")
```

So bleibt das Spiel stabil.
