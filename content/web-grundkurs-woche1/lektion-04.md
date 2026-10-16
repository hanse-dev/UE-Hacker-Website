# Attribute

**Attribute** stehen im Anfangs-Tag und geben einem Element Zusatzangaben. Das Muster ist immer `name="wert"`:

```html
<h2 id="training">Training</h2>
<abbr title="Fédération Internationale de Football Association">FIFA</abbr>
```

| Attribut | Wofür |
|---|---|
| `id` | ein **eindeutiger** Name für genau ein Element – jede id darf nur einmal vorkommen |
| `title` | Zusatztext, der beim Darüberfahren mit der Maus erscheint |
| `lang` | Sprache eines Elements, z. B. `<p lang="en">Hello!</p>` mitten in einer deutschen Seite |

`<abbr>` markiert eine **Abkürzung** – mit `title` steht die ausgeschriebene Bedeutung gleich dabei.

Eine `id` wirst du noch oft brauchen: für Sprungmarken (Woche 3), für Formulare (Woche 4) und für CSS (Woche 5).

> 💡 Werte immer in Anführungszeichen setzen. Mehrere Attribute trennst du mit Leerzeichen: `<p id="intro" lang="de">`.
