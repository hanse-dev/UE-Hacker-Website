# 🐴 Übung 5: JSON-Dateien: dump und load

Mit **`json.dump(daten, datei)`** schreibst du direkt in eine Datei, mit **`json.load(datei)`** liest du sie wieder:

```python
import json

with open("pferd.json", "w") as f:
    json.dump(pferd, f, indent=2)   # indent macht die Datei lesbar

with open("pferd.json", "r") as f:
    geladen = json.load(f)
```

**Ändern und speichern** geht immer in drei Schritten: **laden → ändern → wieder speichern**. Auch ganze Listen von Dictionaries passen in eine JSON-Datei.

> 💡 Umlaute schreibt `json.dump` standardmäßig als `\u00e4` – beim Laden kommt trotzdem wieder ein „ä“ heraus.
