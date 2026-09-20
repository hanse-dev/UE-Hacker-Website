# 🐴 Übung 3: Sicher zugreifen mit get() und in

Wenn ein Schlüssel fehlt, gibt `dict[schlüssel]` einen **KeyError**. Zwei sichere Wege:

```python
print(pferd.get("name"))         # Blitz
print(pferd.get("siege"))       # None – kein Fehler
print(pferd.get("siege", 0))    # 0 – eigener Standardwert

print("name" in pferd)           # True – prüft die SCHLÜSSEL
print("siege" in pferd)         # False
```

**`in`** prüft bei einem Dictionary immer die **Schlüssel**, nie die Werte.
