# 📟 Systemprotokoll 3: if-else

`if-else` bietet **zwei Pfade**: einen für „Bedingung wahr“ und einen für „Bedingung falsch“.

```python
signale = 18
if signale >= 15:
    print("Lebensformen entdeckt!")
else:
    print("Sektor leer.")
```

- `else` braucht **keine Bedingung** – es gilt für alles, was nicht zum `if` passt.
- Auch `else` bekommt einen **Doppelpunkt** und einen **eingerückten** Block.
- Es wird immer **genau einer** der beiden Pfade ausgeführt.

Praktisch, wenn du eine Rechnung in der Meldung brauchst:

```python
energie = 45
verbrauch = 50
if energie >= verbrauch:
    print(f"Sprung möglich! Rest: {energie - verbrauch}%")
else:
    print(f"Sprung unmöglich! Fehlt: {verbrauch - energie}%")
```
