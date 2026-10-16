# Bilder

```html
<img src="/web-bilder/gitarre.svg" alt="Eine rote E-Gitarre" width="160">
```

- `src` – die Adresse des Bildes. In diesem Kurs liegen Bilder unter `/web-bilder/`: `katze`, `hund`, `pferd`, `fisch`, `vogel`, `dino`, `einhorn`, `fussball`, `basketball`, `gitarre`, `buch`, `controller`, `rakete`, `planet`, `pizza`, `blume`, `baum`, `stern` (jeweils mit `.svg`).
- `alt` – der **Alternativtext**: Er beschreibt, was auf dem Bild zu sehen ist. Vorleseprogramme lesen ihn vor, und er erscheint, wenn das Bild nicht lädt.
- `width` bzw. `height` – Größe in Pixeln. Gibst du nur eins an, bleibt das Seitenverhältnis erhalten.

## Guter Alternativtext

Beschreibe, was für das Verständnis wichtig ist: `alt="Gruppenfoto unserer Band auf der Bühne"` statt `alt="Bild"` oder `alt="foto1.jpg"`. Ist ein Bild reine Dekoration, setzt du `alt=""` – dann überspringen Vorleseprogramme es.

## Bild mit Bildunterschrift

```html
<figure>
  <img src="/web-bilder/planet.svg" alt="Der Saturn mit seinen Ringen" width="140">
  <figcaption>Der Saturn hat über 140 Monde.</figcaption>
</figure>
```

`figure` hält Bild und Unterschrift (`figcaption`) zusammen.
