# 📏 Der Abstand zwischen zwei Zahlen

Ab dieser Woche baust du deinen ersten echten Klassifikator: den **k-nächste-Nachbarn**-Algorithmus
(kurz **k-NN**). Die Grundidee: Ein neues Beispiel bekommt das Label seiner "Nachbarn" – der
Trainingsbeispiele, die ihm am ähnlichsten sind.

Um "ähnlich" zu messen, brauchst du einen **Abstand**. Für eine einzelne Zahl ist das einfach:
die Differenz, ohne Vorzeichen. Dafür gibt es die eingebaute Funktion `abs()`.

```python
gewicht_a = 30
gewicht_b = 25
abstand = abs(gewicht_a - gewicht_b)
print(abstand)
```

Je kleiner der Abstand, desto ähnlicher die beiden Werte. Damit kannst du auch vergleichen,
welcher von zwei Nachbarn näher an einem Zielwert liegt:

```python
ziel = 28
nachbar1 = 30
nachbar2 = 10

abstand1 = abs(ziel - nachbar1)
abstand2 = abs(ziel - nachbar2)
print(abstand1)
print(abstand2)
```

`nachbar1` liegt näher an `ziel` – sein Abstand ist kleiner.

> 💡 In den nächsten Lektionen erweiterst du das auf Beispiele mit **mehreren** Merkmalen
> gleichzeitig, so wie die Tier-Datensätze aus Woche 2.
