# Fehlersuche: Flexbox

Wenn Flexbox „nicht funktioniert“, liegt es fast immer an einem dieser drei Fehler:

- **`display: flex` am falschen Element:** Es gehört an den Container, nicht an die Items.
- **Falscher Wert:** CSS ist Englisch – `center`, nicht `centre` oder `mitte`. Ungültige Werte werden stillschweigend ignoriert.
- **Falsche Achse:** `justify-content` wirkt entlang der Hauptachse, `align-items` quer dazu. Bei `flex-direction: column` vertauschen sich die Rollen.
