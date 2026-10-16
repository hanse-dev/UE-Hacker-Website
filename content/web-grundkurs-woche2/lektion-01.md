# Header, Main und Footer

Ein `<div>` ist eine Kiste ohne Bedeutung. HTML hat aber auch Kisten **mit** Bedeutung – sogenannte **semantische Elemente**. Sie verraten, welche Rolle ein Bereich spielt:

```html
<header>
  <h1>FC Hafenkante</h1>
  <nav>…Menü…</nav>
</header>
<main>
  …der eigentliche Inhalt…
</main>
<footer>
  <p>© 2026 FC Hafenkante</p>
</footer>
```

| Element | Bedeutung |
|---|---|
| `header` | Kopf der Seite: Name, Logo, oft das Menü |
| `nav` | Navigation – die wichtigsten Links |
| `main` | der Hauptinhalt; gibt es nur **einmal** pro Seite |
| `footer` | Fuß: Impressum, Kontakt, Copyright |

Auf dem Bildschirm sieht man davon erst einmal nichts – aber Vorleseprogramme können direkt zum Hauptinhalt springen, und Suchmaschinen verstehen deine Seite besser.
