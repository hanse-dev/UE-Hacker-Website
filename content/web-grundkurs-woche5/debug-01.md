# Fehlersuche: CSS

Bei CSS-Fehlern passiert einfach **nichts** – die Regel wirkt nicht. Die häufigsten Ursachen:

- **Fehlendes Semikolon:** `color: red background-color: yellow;` – der Browser versteht beide Zeilen nicht mehr.
- **Falsch geschriebener Name:** `colour` statt `color`, `font-size: 20 px` mit Leerzeichen statt `20px`.
- **Selektor passt nicht:** Groß-/Kleinschreibung zählt (`.Karte` ≠ `class="karte"`), und `.` und `#` sind nicht austauschbar.
