# Entscheidungen mit if 🤔

Bisher hat dein Programm immer einfach alles ausgeführt, was drinstand. Mit `if` kann Python zum ersten Mal selbst entscheiden, was es tun soll – genau wie du im echten Leben: "**Wenn** es regnet, nehme ich einen Regenschirm mit." Wenn die Bedingung wahr ist, wird der eingerückte Code darunter ausgeführt – sonst wird er einfach übersprungen.

```python
punkte = 80
if punkte >= 50:
    print("Bestanden!")
```

Mit `else` gibst du an, was passieren soll, wenn die Bedingung **nicht** wahr ist:

```python
punkte = 30
if punkte >= 50:
    print("Bestanden!")
else:
    print("Leider nicht bestanden.")
```

Zum Vergleichen von Werten gibt es mehrere Zeichen: `==` (ist gleich – Achtung, **zwei** Gleichheitszeichen, nicht wie beim Speichern einer Variable!), `!=` (ist ungleich), `<`, `>`, `<=`, `>=`.

**Ganz wichtig:** Der Code nach `if` und `else` muss eingerückt sein (4 Leerzeichen oder Tab) – die Einrückung zeigt Python, welcher Code zum `if` gehört. Vergisst du sie, meldet Python einen Fehler. Am besten lässt du dir das dein Code-Editor automatisch machen, indem du nach dem Doppelpunkt einfach Enter drückst.
