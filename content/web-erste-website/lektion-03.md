# Bilder und Links

Jetzt wird deine Seite bunter: mit Bildern und mit Links zu anderen Seiten.

## Bilder

Ein Bild bindest du mit `<img>` ein (*image*, Bild):

```html
<img src="/web-bilder/katze.svg" alt="Eine schlafende Katze">
```

- `src` sagt, **wo** das Bild liegt. In diesem Kurs findest du viele Bilder im Ordner `/web-bilder/` – die Liste steht unten.
- `alt` beschreibt das Bild in Worten. Das liest zum Beispiel ein Vorleseprogramm vor, wenn jemand das Bild nicht sehen kann. Deshalb gehört zu **jedem** Bild ein `alt`.

`src` und `alt` heißen **Attribute**: Zusatzangaben, die im Anfangs-Tag stehen. `<img>` hat übrigens **kein** End-Tag – es umschließt ja keinen Text.

**Bilder zum Aussuchen:** `katze`, `hund`, `pferd`, `fisch`, `vogel`, `dino`, `einhorn`, `fussball`, `basketball`, `gitarre`, `buch`, `controller`, `rakete`, `planet`, `pizza`, `blume`, `baum`, `stern` – jeweils mit `.svg` am Ende, zum Beispiel `/web-bilder/rakete.svg`.

Mit `width` machst du ein Bild kleiner oder größer: `<img src="/web-bilder/hund.svg" alt="Ein Hund" width="120">`.

## Links

Ein Link bringt dich mit einem Klick auf eine andere Seite. Dafür gibt es `<a>` (*anchor*, Anker):

```html
<a href="https://de.wikipedia.org/wiki/Hauskatze">Mehr über Katzen</a>
```

- `href` ist die Adresse, zu der der Link führt.
- Der Text zwischen `<a>` und `</a>` ist das, worauf man klickt.

> 💡 In der Vorschau öffnet sich ein Link in einem neuen Tab – so bleibt deine Seite hier stehen.
