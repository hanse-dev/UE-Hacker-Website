# Listen

Listen kennst du schon. Hier sind die Feinheiten:

```html
<ol>
  <li>Aufwärmen</li>
  <li>Passspiel</li>
  <li>Abschlussspiel</li>
</ol>
```

- `<ul>` (*unordered list*): Reihenfolge egal – Punkte
- `<ol>` (*ordered list*): Reihenfolge wichtig – Nummern
- `<li>`: ein Listenpunkt, **nur** direkt in `ul` oder `ol`

## Nützliche Attribute für ol

- `start="5"` – die Zählung beginnt bei 5
- `reversed` – zählt rückwärts, z. B. für einen Countdown deiner Top 3

## Listen in Listen

Ein `li` darf selbst wieder eine Liste enthalten:

```html
<ul>
  <li>Obst
    <ul>
      <li>Äpfel</li>
      <li>Bananen</li>
    </ul>
  </li>
  <li>Gemüse</li>
</ul>
```

Die innere Liste steht **im** `li`, also vor dessen `</li>`.
