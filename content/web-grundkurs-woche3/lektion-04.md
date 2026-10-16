# Tabellen

Für Daten in Zeilen und Spalten – Stundenplan, Ergebnisse, Preisliste – gibt es Tabellen:

```html
<table>
  <caption>Ergebnisse Hallenturnier</caption>
  <thead>
    <tr><th>Team</th><th>Punkte</th></tr>
  </thead>
  <tbody>
    <tr><td>Blau</td><td>9</td></tr>
    <tr><td>Rot</td><td>6</td></tr>
  </tbody>
</table>
```

| Element | Bedeutung |
|---|---|
| `table` | die ganze Tabelle |
| `caption` | Überschrift der Tabelle |
| `thead` / `tbody` | Kopfbereich / Datenbereich |
| `tr` | eine Zeile (*table row*) |
| `th` | eine Kopfzelle (*table header*), meist fett |
| `td` | eine Datenzelle (*table data*) |

Jede Zeile `tr` sollte gleich viele Zellen haben.

> 💡 Tabellen sind für **Daten** da – nicht, um eine Seite zu gestalten. Für Layouts kommen später Flexbox und Grid.
