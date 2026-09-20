# 🧬 Zauberformel 1: Mehrere Parameter

Manche Zauber brauchen mehr als eine Zutat. Du trennst Parameter einfach mit **Kommas**:

```python
def erstelle_charakter(name, klasse, level):
    print(f"Name: {name}")
    print(f"Klasse: {klasse}")
    print(f"Level: {level}")

erstelle_charakter("Aria", "Magierin", 5)
```

**Wichtig:** Die **Reihenfolge** der Argumente muss zur Reihenfolge der Parameter passen. Das erste Argument (`"Aria"`) landet im ersten Parameter (`name`), das zweite (`"Magierin"`) im zweiten (`klasse`) und so weiter.

> ⚠️ Vertauschst du die Argumente, bekommt jeder Parameter den falschen Wert – Python meckert nicht, aber der Zauber geht schief: `erstelle_charakter(5, "Aria", "Magierin")` gibt Unsinn aus!

Außerdem gilt: Übergib **genauso viele** Argumente, wie die Funktion Parameter hat – sonst gibt es eine Fehlermeldung.
