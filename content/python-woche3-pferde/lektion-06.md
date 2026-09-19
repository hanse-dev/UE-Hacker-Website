# 🪆 Übung 6: Verschachtelte Bedingungen

Eine Bedingung darf **eine weitere Bedingung enthalten** – das nennt man **Verschachtelung**. Jede zusätzliche Ebene wird **einen Schritt weiter eingerückt**:

```python
stalltuer_verschlossen = True
richtiger_schluessel = True

if stalltuer_verschlossen:
    print("Die Stalltür ist verschlossen.")
    if richtiger_schluessel:
        print("Der Schlüssel passt – die Stalltür öffnet sich!")
    else:
        print("Dieser Schlüssel passt nicht.")
else:
    print("Die Stalltür steht bereits offen.")
```

Die innere Frage wird nur gestellt, wenn die äußere schon mit `True` beantwortet wurde. Jedes `else` gehört zu dem `if`, das **gleich weit eingerückt** ist.

> ⚠️ Achte genau auf die Einrückung – sie entscheidet, welcher Code zu welcher Bedingung gehört!
