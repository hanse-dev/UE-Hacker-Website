# 🃏 Modul-Protokoll 3: Zufällig auswählen und mischen

Mit Listen aus Woche 6 kann `random` noch mehr:

```python
import random

module = ["Navigation", "Kommunikation", "Antrieb", "Lebenserhaltung", "Sensoren"]
eins = random.choice(module)         # ein zufälliger Eintrag
drei = random.sample(module, 3)      # 3 verschiedene Einträge (ohne Wiederholung)
mischung = module.copy()
random.shuffle(mischung)               # mischt die Liste selbst (gibt nichts zurück!)
```

- **`random.choice(liste)`** – ein Eintrag
- **`random.sample(liste, k)`** – `k` **verschiedene** Einträge
- **`random.shuffle(liste)`** – **verändert** die Liste selbst; willst du das Original behalten, mische vorher eine Kopie (`liste.copy()`)

> ⚠️ Schreibe nicht `liste = random.shuffle(liste)` – `shuffle` gibt nichts zurück, danach wäre `liste` gleich `None`.
