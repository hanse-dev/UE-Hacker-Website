# Fehlersuche: Feinschliff

Zum Schluss noch drei Fehler, die auch erfahrenen Leuten passieren:

- **Der Hover-Übergang ist nur in eine Richtung sanft:** Die `transition` steht in der `:hover`-Regel statt am Element selbst.
- **Ein Menü-Link springt nicht:** `href="#galerie"`, aber die id heißt `Galerie` – Groß- und Kleinschreibung zählt.
- **Der Dunkelmodus-Knopf tut nichts Sichtbares:** JavaScript schaltet eine Klasse um, die im CSS anders heißt.
