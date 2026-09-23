# 🚀 Daten-Log 4: JSON-Text: dumps und loads

**JSON** ist ein Textformat, das fast aussieht wie ein Python-Dictionary. Fast jedes Programm der Welt versteht es. Das Modul **`json`** übersetzt in beide Richtungen:

```python
import json

mitglied = {"name": "Nova", "rang": 4}
text = json.dumps(mitglied)      # Dictionary → JSON-Text (String)
zurueck = json.loads(text)      # JSON-Text → Dictionary
print(zurueck["name"])          # Nova
```

**Merkhilfe:** das **s** in `dumps`/`loads` steht für **String**. Die Varianten ohne s (`dump`/`load`) arbeiten mit Dateien – die kommen in der nächsten Lektion.

> 💡 JSON kennt **keine Tupel**: Aus `(3, 4)` wird beim Zurücklesen die **Liste** `[3, 4]`. Ein Wert `True` wird im Text zu `true`.
