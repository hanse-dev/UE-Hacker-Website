# 🗣️ Zauberformel 1: f-Strings

Willkommen zurück, Abenteurer! Am Rand von Pyralia erhebt sich der **Elementarturm** – nur wer alle **vier Elemente** beherrscht, darf ihn betreten. Die **Turmwächterin** erwartet dich mit einer klaren Ansage: *"Jedes Element hat seine eigene Natur. Wer sie verwechselt, dessen Zauber misslingt."*

Bevor du Elemente kombinierst, brauchst du eine Sprache, um über sie zu sprechen. Ein **f-String** ist die moderne und lesbare Art, Variablen in Text einzubauen. Das `f` vor den Anführungszeichen sagt Python: *"Schau in die geschweiften Klammern!"*

```python
name = "Aria"
level = 5
print(f"Hallo {name}! Du bist Level {level}!")
```

In die `{ }` darfst du sogar **rechnen**:

```python
gold = 100
bonus = 25
print(f"Dein Gold: {gold + bonus}")
```

| Methode | Beispiel | Empfehlung |
|---------|---------|------------|
| `+`-Verkettung | `"Hallo " + name` | funktioniert, braucht `str()` für Zahlen |
| f-String | `f"Hallo {name}"` | moderner, kürzer, Zahlen funktionieren direkt |

> ✅ Benutze f-Strings – sie sind klarer zu lesen und weniger fehleranfällig. Die `+`-Methode aus Woche 1 funktioniert aber weiterhin.
