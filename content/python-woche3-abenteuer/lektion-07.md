# ⚖️ Zauberformel 5: Verschachtelte Bedingungen

Ein `if` darf ein weiteres `if` **enthalten**. Man nennt das **Verschachtelung** – wie Türen hinter Türen. Die innere Prüfung passiert nur, wenn die äußere wahr war.

```python
tuer_verschlossen = True
richtiger_schluessel = True

if tuer_verschlossen:
    print("Die Tür ist verschlossen.")
    if richtiger_schluessel:
        print("Der Schlüssel passt – die Tür öffnet sich!")
    else:
        print("Dieser Schlüssel passt nicht.")
else:
    print("Die Tür steht bereits offen.")
```

**Die Macht der Einrückung:** Jede zusätzliche Ebene braucht **4 weitere Leerzeichen**. Am Einrücken erkennt Python (und du), welcher `else` zu welchem `if` gehört.

> Tipp: Oft kannst du verschachtelte Bedingungen auch mit `and` schreiben. Verschachteln lohnt sich, wenn du zwischen den Prüfungen noch etwas ausgeben willst.
