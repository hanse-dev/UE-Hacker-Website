# 🔗 Systemprotokoll 4: Texte verbinden

Auch Strings kannst du „verrechnen":

- **`+`** klebt zwei Texte aneinander (**Verketten**): `"Neo" + "tron"` ergibt `"Neotron"`
- **`*`** wiederholt einen Text: `"Ping" * 3` ergibt `"PingPingPing"`

```python
prefix = "Neo"
suffix = "tron"
print(prefix + suffix)   # Neotron
print(prefix * 3)        # NeoNeoNeo
```

> 📡 **Merke:** Nicht alle Typen passen zusammen! `"Neo" + 5` (Text plus Zahl) ist ein Fehler. Im nächsten Protokoll lernst du, wie du Typen ineinander umwandelst.
