# Fehlersuche: Boxen

Box-Fehler erkennst du daran, dass etwas **zu breit** ist oder **am falschen Ort** sitzt:

- **Eine Box ragt über den Rand:** `width: 100%` plus `padding` und `border` ist breiter als 100 % – es fehlt `box-sizing: border-box`.
- **`margin: 0 auto` zentriert nicht:** Die Box ist so breit wie ihr Platz. Ohne `width` oder `max-width` gibt es nichts zu verteilen.
- **Ein absolutes Element sitzt in der Ecke der Seite statt in der Karte:** Der Karte fehlt `position: relative`.
