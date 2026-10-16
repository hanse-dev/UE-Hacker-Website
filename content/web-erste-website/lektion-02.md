# Ordnung auf der Seite

Eine gute Website ist wie ein gut sortiertes Heft: Überschriften zeigen, wo ein neues Thema beginnt, und Listen machen Aufzählungen übersichtlich.

## Überschriften in Stufen

Neben `<h1>` gibt es kleinere Überschriften: `<h2>`, `<h3>` bis hinunter zu `<h6>`. Die Zahl sagt, wie wichtig die Überschrift ist:

```html
<h1>Meine Katze Mia</h1>
<h2>Was Mia gerne frisst</h2>
<h2>Mias Lieblingsplätze</h2>
```

- `<h1>` gibt es meistens nur **einmal** – das ist der Titel der ganzen Seite.
- Mit `<h2>` teilst du die Seite in Abschnitte ein.

## Listen

Für Aufzählungen gibt es Listen. Jeder Punkt steht in einem eigenen `<li>` (*list item*, Listenpunkt):

```html
<ul>
  <li>Thunfisch</li>
  <li>Hühnchen</li>
  <li>Katzenmilch</li>
</ul>
```

- `<ul>` macht eine Liste mit Punkten.
- `<ol>` macht eine **nummerierte** Liste – praktisch für eine Rangliste oder eine Anleitung.

## Wichtiges hervorheben

- `<strong>` macht Text **fett**: `Mia ist <strong>sehr</strong> neugierig.`
- `<em>` macht Text *schräg* und betont ihn: `Sie schläft <em>immer</em> in der Sonne.`

> 💡 Tags dürfen ineinander stecken – wie Schachteln in Schachteln. Wichtig ist nur: Was zuletzt aufgemacht wurde, wird zuerst wieder zugemacht.
