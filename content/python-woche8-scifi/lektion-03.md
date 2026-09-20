# 🚀 Daten-Log 3: Sicher zugreifen mit get() und in

Wenn ein Schlüssel fehlt, gibt `dict[schlüssel]` einen **KeyError**. Zwei sichere Wege:

```python
print(mitglied.get("name"))         # Nova
print(mitglied.get("schild"))       # None – kein Fehler
print(mitglied.get("schild", 0))    # 0 – eigener Standardwert

print("name" in mitglied)           # True – prüft die SCHLÜSSEL
print("schild" in mitglied)         # False
```

**`in`** prüft bei einem Dictionary immer die **Schlüssel**, nie die Werte.
