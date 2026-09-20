# 🃏 Archiv-Zauber 3: Zufällig auswählen und mischen

Mit Listen aus Woche 6 kann `random` noch mehr:

```python
import random

regale = ["Regal der Elemente", "Regal der Tiere", "Regal der Sterne", "Regal der Schatten", "Regal der Helden"]
eins = random.choice(regale)         # ein zufälliger Eintrag
drei = random.sample(regale, 3)      # 3 verschiedene Einträge (ohne Wiederholung)
mischung = regale.copy()
random.shuffle(mischung)               # mischt die Liste selbst (gibt nichts zurück!)
```

- **`random.choice(liste)`** – ein Eintrag
- **`random.sample(liste, k)`** – `k` **verschiedene** Einträge
- **`random.shuffle(liste)`** – **verändert** die Liste selbst; willst du das Original behalten, mische vorher eine Kopie (`liste.copy()`)

> ⚠️ Schreibe nicht `liste = random.shuffle(liste)` – `shuffle` gibt nichts zurück, danach wäre `liste` gleich `None`.
