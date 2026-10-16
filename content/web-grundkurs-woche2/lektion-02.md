# Section und Article

Im `main` gibt es oft mehrere Themen. Dafür gibt es zwei weitere Elemente:

- **`section`** – ein **Abschnitt** zu einem Thema. Er beginnt fast immer mit einer Überschrift (`h2`).
- **`article`** – ein **in sich geschlossener** Beitrag, der auch allein stehen könnte: ein Spielbericht, ein Blogpost, eine Buchempfehlung.

```html
<main>
  <section>
    <h2>Mannschaften</h2>
    <p>Wir haben drei Teams.</p>
  </section>
  <section>
    <h2>Neuigkeiten</h2>
    <article>
      <h3>3:1-Sieg am Samstag</h3>
      <p>Unsere U14 hat das Derby gewonnen.</p>
    </article>
  </section>
</main>
```

Die Überschriften bilden eine **Hierarchie**: `h1` für die Seite, `h2` für Abschnitte, `h3` für Beiträge darin. Spring dabei keine Ebene über – also nicht von `h1` direkt zu `h4`.
