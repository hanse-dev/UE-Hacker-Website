## 🔤 Übung 4: Buchstaben durchlaufen

Eine for-Schleife kann auch **Text** durchgehen – Buchstabe für Buchstabe:

```python
name = "Thunder"
for buchstabe in name:
    print(f"  - {buchstabe}")
```

Bei jedem Durchlauf enthält `buchstabe` den nächsten Buchstaben des Pferdenamens. Die Schleife endet, wenn kein Buchstabe mehr übrig ist.

> 🐴 Das funktioniert, weil Text eine **Folge von Zeichen** ist – genau wie `range()` eine Folge von Zahlen liefert.
