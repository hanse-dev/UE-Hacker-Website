# ⭐ Muster aus Sternen

Verschachtelte Schleifen sind ideal für **Muster**: Die äußere Schleife steht für die **Zeilen**, die innere für die **Spalten**.

Normalerweise springt `print()` nach jeder Ausgabe in eine neue Zeile. Mit `end=""` (oder `end=" "`) bleibt der Cursor stattdessen in derselben Zeile. Ein leeres `print()` beendet die Zeile:

```python
for zeile in range(3):
    for spalte in range(4):
        print("⭐", end=" ")
    print()
```

Das zeichnet ein Rechteck aus 3 Zeilen mit je 4 Sternen.

**Tipp:** Wenn die Anzahl der inneren Durchläufe von der Zeile abhängt (`range(zeile)`), entsteht ein **Dreieck**!
