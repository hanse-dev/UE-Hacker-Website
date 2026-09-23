# Was ist eine Vigenère-Chiffre?

Du kennst schon die Cäsar-Chiffre: Jeder Buchstabe wird um eine **feste** Anzahl Stellen verschoben. Das Problem: Es gibt nur 26 mögliche Verschiebungen – ein Angreifer kann einfach alle durchprobieren (das hast du im Cäsar-Projekt selbst gemacht).

Die Vigenère-Chiffre löst dieses Problem: Statt einer einzigen Zahl benutzt sie ein ganzes **Schlüsselwort**, z.B. `"key"`. Jeder Buchstabe des Schlüsselworts liefert seine eigene Verschiebung – genau wie bei Cäsar berechnet: die Position des Buchstabens im Alphabet.

```python
print(ord('k') - ord('a'))   # 10 – 'k' verschiebt um 10
print(ord('e') - ord('a'))   # 4  – 'e' verschiebt um 4
print(ord('y') - ord('a'))   # 24 – 'y' verschiebt um 24
```

Das Schlüsselwort `"key"` liefert also drei verschiedene Verschiebungen: 10, 4, 24. Damit verschlüsselst du nicht mehr jeden Buchstaben gleich – schon das macht die Chiffre deutlich schwerer zu knacken.

> 💡 `ord()` und `chr()` kennst du schon aus [Lektion 1 deines Cäsar-Chiffre-Projekts](/kurs/projekt-caesar-chiffre).
