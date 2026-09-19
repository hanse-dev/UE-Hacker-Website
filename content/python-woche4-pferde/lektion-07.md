## 🌀 Übung 7: Der Trainingsplan-Zirkel

Eine Schleife kann eine weitere Schleife **enthalten**. Die innere Schleife läuft dann bei **jedem** Durchlauf der äußeren komplett durch:

```python
for woche in range(1, 4):
    print(f"Trainingswoche {woche}:")
    for einheit in range(1, 3):
        print(f"  Einheit {einheit} wird absolviert...")
```

3 Wochen × 2 Einheiten = 6 Einheiten-Meldungen.

So entstehen Muster aus Hufabdrücken:

```python
for zeile in range(3):
    for spalte in range(4):
        print("🐴", end=" ")
    print()
```

- `end=" "` hängt statt eines Zeilenumbruchs ein Leerzeichen an.
- `end=""` hängt gar nichts an, das nächste `print` macht direkt in derselben Zeile weiter.
- Das leere `print()` am Ende jeder Zeile macht den Zeilenumbruch.

> 🐴 **Wichtig:** Jede zusätzliche Verschachtelungsebene braucht eine **weitere Einrückung**!
