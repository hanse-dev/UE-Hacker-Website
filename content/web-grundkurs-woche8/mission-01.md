# Mission: Responsive Galerie

Bau eine Galerie-Seite zu deinem Thema, die auf Handy und Laptop gut aussieht:

- das **viewport-meta-Tag** im `head`
- eine Überschrift und mindestens **sechs** Bilder aus `/web-bilder/` mit Alternativtext in einem Container mit `class="galerie"`
- die Galerie ist ein **Grid**, das sich selbst anpasst: `repeat(auto-fill, minmax(…, 1fr))`
- das erste Bild (`class="highlight"`) ist **zwei Spalten** breit
- Bilder werden nie breiter als ihr Platz (`max-width: 100%`)
- eine **Media Query** für Bildschirme bis 600px, die etwas ändert (zum Beispiel die Überschrift kleiner macht)
