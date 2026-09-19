# 🌿 Übung 4: if-elif-else

Manchmal reichen zwei Wege nicht. Mit **`elif`** (kurz für „else if") prüfst du weitere Bedingungen nacheinander:

```python
erfahrung = 750
if erfahrung >= 1000:
    print("Meisterreiter!")
elif erfahrung >= 500:
    print("Fortgeschrittener Reiter!")
elif erfahrung >= 100:
    print("Anfänger!")
else:
    print("Noch viel zu üben...")
```

> 🐴 **Wichtig:** `elif` braucht **immer eine Bedingung**. Python prüft von oben nach unten und führt nur den **ersten wahren** Weg aus – alle weiteren werden übersprungen. `else` am Ende fängt alles andere auf.

Deshalb kommt die **strengste Bedingung zuerst**: Bei `erfahrung = 750` wäre `>= 100` auch wahr, aber `>= 500` kommt früher dran.
