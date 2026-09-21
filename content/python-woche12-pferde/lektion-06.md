# 🐴 Etappe 6: Falsche Eingaben abfangen

*Wissen aus Woche 8: try/except*

Spieler tippen manchmal Unsinn. Ein Befehl wie `gehe norden` besteht aus zwei Wörtern, die `split()` in `action` und `target` zerlegt. Bei `hallo` passt die Anzahl nicht, und Python wirft einen `ValueError`. `try/except` fängt ihn ab:

```python
def fuehre_aus(spieler, text):
    try:
        action, target = text.split()
    except ValueError:
        print("🤔 Ich verstehe nur Befehle aus zwei Wörtern, z.B. 'gehe norden' oder 'nimm Taschenlampe'.")
        return
    if action == "gehe":
        spieler.gehe(target)
        pruefe_gegner(spieler)
    elif action == "nimm":
        spieler.nimm(target)
    else:
        print(f"🤔 '{action}' kenne ich nicht. Versuche 'gehe' oder 'nimm'.")
```

So bleibt das Spiel stabil.
