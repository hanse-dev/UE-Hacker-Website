# 📟 Systemprotokoll 6: Verschachtelte Bedingungen

Eine `if`-Bedingung darf eine weitere `if`-Bedingung **enthalten** – das nennt man **Verschachtelung**. So triffst du erst eine grobe, dann eine feine Entscheidung.

```python
schleuse_verriegelt = True
richtiger_code = True

if schleuse_verriegelt:
    print("Die Schleuse ist verriegelt.")
    if richtiger_code:
        print("Der Code stimmt – die Schleuse öffnet sich!")
    else:
        print("Falscher Code! Zugang verweigert.")
else:
    print("Die Schleuse steht bereits offen.")
```

**Jede zusätzliche Ebene braucht eine weitere Einrückung.** Die Einrückung zeigt dir und Python, welches `else` zu welchem `if` gehört: Das innere `else` steht auf gleicher Höhe wie das innere `if`, das äußere `else` auf gleicher Höhe wie das äußere `if`.

> 📡 **Merke:** Erst die äußere Bedingung, dann die innere. Ist die äußere falsch, wird die innere gar nicht erst geprüft.

🎉 Du hast alle Protokolle dieser Woche gelernt – jetzt bist du bereit für Debug, Missionen und die Extra-Herausforderungen!
