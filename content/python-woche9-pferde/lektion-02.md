# 🐴 Übung 2: Zeilenweise lesen und anhängen

Bei größeren Dateien gehst du **Zeile für Zeile** durch – die Datei selbst ist eine Schleife:

```python
with open("stallbuch.txt", "r") as f:
    for zeile in f:
        print(zeile.strip())       # strip() entfernt das \n am Ende

with open("stallbuch.txt", "a") as f:     # "a" = anhängen, nichts wird gelöscht
    f.write("Update: Turnier gewonnen\n")

teile = "Blitz,8".split(",")   # Text an Kommas zerlegen: ["Blitz", "8"]
```

| Modus | Bedeutung |
|---|---|
| `"r"` | lesen |
| `"w"` | schreiben, **überschreibt** die Datei |
| `"a"` | anhängen ans Ende |

`f.readlines()` liefert alle Zeilen auf einmal als **Liste**.
