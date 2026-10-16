# Text auszeichnen

Für Hervorhebungen gibt es mehrere Elemente – jedes mit eigener **Bedeutung**:

| Element | Bedeutung | sieht meist so aus |
|---|---|---|
| `strong` | besonders **wichtig** | fett |
| `em` | **betont** (beim Vorlesen anders gesprochen) | kursiv |
| `mark` | **markiert** – wie mit dem Textmarker | gelb hinterlegt |
| `small` | Kleingedrucktes, Randbemerkung | kleiner |

Für Zitate gibt es `blockquote` (ein ganzer Absatz) mit `cite` für die Quelle:

```html
<blockquote>
  <p>Fantasie ist wichtiger als Wissen.</p>
</blockquote>
<p><cite>Albert Einstein</cite></p>
```

> 💡 Wähle das Element nach der **Bedeutung**, nicht nach dem Aussehen. Wie etwas aussieht, regelst du später mit CSS.
