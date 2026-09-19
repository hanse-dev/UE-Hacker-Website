# 🚀 Woche 3 – Die Pfade der Entscheidung

Willkommen zurück, Kommandant:in! Du erreichst den **Knotenpunkt des Universums** – ein Ort, an dem jede Entscheidung über die Zukunft der Galaxie entscheidet. In dieser Woche lernst du:

1. **if** – Code nur ausführen, wenn etwas stimmt
2. **Vergleichsoperatoren** wie `==`, `!=`, `<`, `>`, `<=`, `>=`
3. **if-else** – zwei Wege
4. **if-elif-else** – viele Wege
5. **and, or, not** – Bedingungen verknüpfen
6. **Verschachtelte Bedingungen** – Entscheidung in der Entscheidung

## 📟 Systemprotokoll 1: if

`if` prüft eine Bedingung und führt Code **nur aus, wenn die Bedingung wahr ist** (also `True` ergibt).

```python
sicherheitsstufe = 5
if sicherheitsstufe == 5:
    print("Zugriff auf Hauptsystem gewährt!")
```

Achte auf zwei Dinge:

- Hinter der Bedingung steht ein **Doppelpunkt `:`**
- Der Code, der dazugehört, wird **eingerückt** (4 Leerzeichen oder Tab-Taste). Die Einrückung zeigt Python, was zum `if` gehört.

Auch eine Boolean-Variable (aus Woche 2) kannst du direkt als Bedingung nutzen:

```python
system_online = True
if system_online:
    print("Alle Systeme operational.")
```

Ist die Bedingung nicht wahr, überspringt Python den eingerückten Block einfach.

> 📡 **Merke:** Doppelpunkt nach der Bedingung und eingerückter Block – ohne beides läuft nichts!
