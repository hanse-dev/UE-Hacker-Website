# 🚀 Daten-Log 5: Tupel

Ein **Tupel** ist wie eine Liste, aber **unveränderlich**. Du schreibst es mit runden Klammern:

```python
bauteil = ("Schildmodul", 15, "Energie")
print(bauteil[0])          # Schildmodul – Zugriff über die Position wie bei Listen
print(len(bauteil))        # 3

name, wert, sorte = bauteil   # Unpacking: drei Variablen auf einmal
einzel = (42,)                 # Ein-Element-Tupel braucht das Komma!
```

**Schritt für Schritt:**
1. **`(a, b, c)`** – runde Klammern, Kommas dazwischen
2. **`tupel[0]`** – Zugriff über die Position
3. **`x, y = tupel`** – Unpacking verteilt die Werte auf Variablen (Anzahl muss passen)

Tupel eignen sich für Dinge, die zusammengehören und fest bleiben – zum Beispiel Koordinaten `(x, y)`.
