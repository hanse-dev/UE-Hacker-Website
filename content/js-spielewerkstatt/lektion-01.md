# Dein Spielfeld: Schläger und Ball

Willkommen in der JS-Spielewerkstatt! Du baust hier Schritt für Schritt dein eigenes
Browserspiel – und schon in dieser ersten Lektion siehst du die echte Spielszene: Schläger unten,
Ball oben. Kein Zwischenschritt mit einer einzelnen, bedeutungslosen Form – von Anfang an das
echte Bild.

Die Sprache dafür ist **JavaScript**. Auf dieser Seite hast du unten ein eigenes **Spielfeld**
(ein `<canvas>`-Element). Dein Code läuft in einem abgeschotteten Bereich und zeichnet direkt
darauf.

So holst du dir das Spielfeld und bereitest es zum Zeichnen vor:

```js
const canvas = document.getElementById('spielfeld');
const ctx = canvas.getContext('2d');
```

`ctx` ist dein Zeichenstift. Rechtecke zeichnest du mit `fillRect(x, y, breite, hoehe)` –
`(0, 0)` ist oben links, x wächst nach rechts, y wächst nach unten. Kreise zeichnest du mit
`arc(x, y, radius, start, ende)` – für einen ganzen Kreis nimmst du `0` bis `Math.PI * 2`.

Damit du das Zeichnen des Schlägers und des Balls später wiederverwenden kannst (du brauchst es
in jeder weiteren Lektion wieder), verpackst du es gleich in zwei **Funktionen**. Eine Funktion
ist ein Stück Code mit einem Namen, das Werte als **Parameter** entgegennimmt:

```js
function zeichneSchlaeger(ctx, x) {
  ctx.fillStyle = 'dodgerblue';
  ctx.fillRect(x, 270, 80, 12);
}

function zeichneBall(ctx, x, y) {
  ctx.fillStyle = 'orange';
  ctx.beginPath();
  ctx.arc(x, y, 10, 0, Math.PI * 2);
  ctx.fill();
}
```

Definiert ist damit noch nichts gezeichnet – erst der **Aufruf** mit konkreten Werten zeichnet
wirklich:

```js
zeichneSchlaeger(ctx, 160);   // Schläger bei x = 160
zeichneBall(ctx, 200, 20);    // Ball bei x = 200, y = 20
```

Der Vorteil: in den nächsten Lektionen rufst du `zeichneSchlaeger(...)` und `zeichneBall(...)`
einfach mit neuen Werten auf, statt den Zeichen-Code jedes Mal neu zu schreiben.

> 💡 Falls dir Funktionen/Parameter noch nicht so vertraut sind: [Woche 4 des
> JS-Grundkurses](/kurs/js-grundkurs?week=4) erklärt sie ausführlich von Grund auf – dieser
> Kurs setzt sie als bekannt voraus und nutzt sie direkt am echten Spiel.

> 💡 Jeder Klick auf „Ausführen" oder „Prüfen" startet deinen Code in einem frischen, leeren
> Spielfeld – frühere Zeichnungen sind dann weg. Das ist Absicht: so fängt jede Aufgabe sauber
> von vorne an. Deshalb steht in jeder Aufgabe dieses Kurses der **komplette** Code für die
> Szene, nicht nur der neue Teil – kopiere bestehenden Code also nicht weg, sondern baue direkt
> darin weiter.
