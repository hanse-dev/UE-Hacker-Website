# Fehlersuche: Grid und Handy

- **Das Raster bleibt eine einzige Spalte:** `display: grid` fehlt am Container – `grid-template-columns` allein bewirkt nichts.
- **Die Media Query wirkt nie:** Die Bedingung braucht **runde Klammern**: `@media (max-width: 600px)`, nicht `@media max-width: 600px`.
- **Auf dem Handy muss man waagerecht scrollen:** Ein Bild oder eine Box hat eine feste Breite, die größer ist als der Bildschirm. `max-width: 100%` hilft.
