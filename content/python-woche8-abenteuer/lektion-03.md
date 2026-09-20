# ⚔️ Archiv-Zauber 3: Sicher zugreifen mit get() und in

Wenn ein Schlüssel fehlt, gibt `dict[schlüssel]` einen **KeyError**. Zwei sichere Wege:

```python
print(held.get("name"))         # Aria
print(held.get("mana"))       # None – kein Fehler
print(held.get("mana", 0))    # 0 – eigener Standardwert

print("name" in held)           # True – prüft die SCHLÜSSEL
print("mana" in held)         # False
```

**`in`** prüft bei einem Dictionary immer die **Schlüssel**, nie die Werte.
