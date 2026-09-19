# 🔤 Übung 7: Rechnen mit Texten

Auch Strings kennen Rechenzeichen:

- **`+`** klebt Texte zusammen: `"Sternen" + "prinz"` ergibt `"Sternenprinz"`
- **`*`** wiederholt einen Text: `"Hü! " * 3` ergibt `"Hü! Hü! Hü! "`

```python
name = "Sternen"
zusatz = "prinz"
voll_name = name + zusatz
print(f"Voller Name: {voll_name}")
print(f"Wiehern: {name * 3}")
```

> ⚠️ Text und Zahl lassen sich **nicht** mit `+` mischen (`"Alter: " + 5` ergibt einen Fehler). Dafür brauchst du `str()` oder einen f-String – mehr dazu in der nächsten Übung.
