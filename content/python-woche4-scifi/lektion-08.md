# 📟 Systemprotokoll 8: Muster aus Sternen

Verschachtelte Schleifen sind ideal für **Muster**: Die äußere Schleife steht für die **Zeilen**, die innere für die **Spalten**.

Hängt die Anzahl der inneren Durchläufe von der Zeile ab (`range(zeile)`), entsteht statt eines Rechtecks eine **Treppe**:

```python
for zeile in range(1, 4):
    for spalte in range(zeile):
        print("✨", end=" ")
    print()
```

Zeile 1 bekommt einen Funken, Zeile 2 zwei, Zeile 3 drei.

> 💡 Die Schleifenvariable der inneren Schleife kannst du auch ausgeben: `print(spalte, end="")` schreibt Zahlen statt Sterne.
