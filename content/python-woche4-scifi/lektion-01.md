# 🚀 Woche 4 – Schleifen: Der Zyklus der Zeit

Willkommen, Kommandant:in! Du erreichst den **Chronos-Turm** – ein Ort, an dem Zeit sich wiederholt und Zyklen die Realität programmieren. In dieser Woche lernst du die **Zeit-Zyklen**:

- Die **for-Schleife** für kontrollierte Wiederholungen
- Die **while-Schleife** für flexible Bedingungen
- `range()` für präzise Zeit-Messungen
- **Verschachtelte Schleifen** für komplexe Zeit-Muster

## 📟 Systemprotokoll 1: Die for-Schleife – der Zeit-Loop

Eine **for-Schleife** wiederholt Code für jedes Element einer Folge:

```python
for i in range(5):
    print(f"Zeit-Zyklus {i+1}: Systeme synchronisiert")
```

1. **`for`** startet den Zeit-Loop
2. **`i`** ist ein Platzhalter, der bei jedem Durchlauf die aktuelle Zahl enthält
3. **`range(5)`** liefert die Zahlen 0, 1, 2, 3, 4
4. **`:`** beendet die Schleifen-Definition
5. Der **eingerückte Code** darunter wird bei jedem Durchlauf ausgeführt

> 💡 `range(5)` startet bei 0 und hört *vor* 5 auf – also ist `i` gleich 0, 1, 2, 3, 4. Deshalb geben wir `i+1` aus, um von 1 bis 5 zu zählen.
