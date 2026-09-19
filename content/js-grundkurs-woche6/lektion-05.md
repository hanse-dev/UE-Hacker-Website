# Objekte, Schleifen und Bedingungen kombinieren

Wie bei einfachen Arrays (Woche 5) zeigt sich die Stärke erst richtig, wenn du eine Schleife über
ein Array aus Objekten mit einer Bedingung kombinierst – so wertest du gezielt nur bestimmte
Objekte aus:

```js
let tiere = [
  { name: 'Bello', art: 'Hund' },
  { name: 'Mimi', art: 'Katze' },
  { name: 'Rex', art: 'Hund' },
];

let anzahlHunde = 0;
for (const tier of tiere) {
  if (tier.art === 'Hund') {
    anzahlHunde++;
  }
}
console.log(`Hunde: ${anzahlHunde}`);
```

Die Bedingung `tier.art === 'Hund'` prüft bei jedem Durchlauf eine Property des aktuellen
Objekts – nur Objekte, die passen, werden gezählt (oder summiert, oder sonst irgendwie
ausgewertet). Das ist die Grundlage für fast jede Auswertung einer echten Datenliste.
