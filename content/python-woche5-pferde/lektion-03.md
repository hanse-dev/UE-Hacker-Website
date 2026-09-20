# 🏇 Übung 3: Mehrere Parameter

Manche Übungen brauchen mehr als eine Zutat. Du trennst Parameter einfach mit **Kommas**:

```python
def stelle_pferd_vor(name, rasse, alter):
    print(f"Name: {name}")
    print(f"Rasse: {rasse}")
    print(f"Alter: {alter}")

stelle_pferd_vor("Sturmwind", "Hannoveraner", 6)
```

**Wichtig:** Die **Reihenfolge** der Argumente muss zur Reihenfolge der Parameter passen. Das erste Argument (`"Sturmwind"`) landet im ersten Parameter (`name`), das zweite im zweiten (`rasse`) und so weiter.

> ⚠️ Vertauschst du die Argumente, bekommt jeder Parameter den falschen Wert – Python meckert nicht, aber die Ausgabe ist Unsinn: `stelle_pferd_vor(6, "Sturmwind", "Hannoveraner")`!

Außerdem gilt: Übergib **genauso viele** Argumente, wie die Funktion Parameter hat – sonst gibt es eine Fehlermeldung.
