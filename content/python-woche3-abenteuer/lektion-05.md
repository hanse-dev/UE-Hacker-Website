# ⚖️ Zauberformel 3: if-elif-else

Bei mehr als zwei Möglichkeiten hilft `elif` (Kurzform von *else if*, "sonst wenn"). Python prüft die Bedingungen **von oben nach unten** und führt nur den **ersten** wahren Zweig aus:

```python
xp = 750
if xp >= 1000:
    print("Meister!")
elif xp >= 500:
    print("Fortgeschritten!")
elif xp >= 100:
    print("Anfänger!")
else:
    print("Noch viel zu lernen...")
```

- `elif` braucht **immer eine Bedingung** (ein `elif:` ohne Bedingung ist ein Fehler)
- Du kannst beliebig viele `elif` verwenden
- Das `else` am Ende ist optional und fängt **alles Übrige** auf
- **Die Reihenfolge zählt:** Bei `xp = 750` sind sowohl `xp >= 500` als auch `xp >= 100` wahr – aber nur der erste Treffer gilt. Prüfe deshalb immer von streng nach locker.
