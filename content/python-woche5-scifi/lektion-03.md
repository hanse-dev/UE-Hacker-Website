# 🛰️ Systemprotokoll 3: Mehrere Parameter

Manche Protokolle brauchen mehr als eine Eingabe. Du trennst Parameter einfach mit **Kommas**:

```python
def registriere_crew(name, rolle, level):
    print(f"Name: {name}")
    print(f"Rolle: {rolle}")
    print(f"Level: {level}")

registriere_crew("Nova", "Pilotin", 5)
```

**Wichtig:** Die **Reihenfolge** der Argumente muss zur Reihenfolge der Parameter passen. Das erste Argument (`"Nova"`) landet im ersten Parameter (`name`), das zweite im zweiten (`rolle`) und so weiter.

> ⚠️ Vertauschst du die Argumente, bekommt jeder Parameter den falschen Wert – Python meckert nicht, aber die Ausgabe ist Unsinn: `registriere_crew(5, "Nova", "Pilotin")`!

Außerdem gilt: Übergib **genauso viele** Argumente, wie die Funktion Parameter hat – sonst gibt es eine Fehlermeldung.
