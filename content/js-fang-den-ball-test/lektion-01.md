# Dein Spielfeld: Schläger und Ball

Willkommen im Test-Kurs „Fang den Ball"! Du baust hier Schritt für Schritt dein eigenes
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
`(0, 0)` ist oben links, x wächst nach rechts, y wächst nach unten:

```js
ctx.fillStyle = 'dodgerblue';
ctx.fillRect(160, 270, 80, 12);   // der Schläger: unten im Spielfeld
```

Kreise zeichnest du mit `arc(x, y, radius, start, ende)` – für einen ganzen Kreis nimmst du
`0` bis `Math.PI * 2`:

```js
ctx.fillStyle = 'orange';
ctx.beginPath();
ctx.arc(200, 20, 10, 0, Math.PI * 2);
ctx.fill();   // der Ball: ein Kreis oben im Spielfeld
```

> 💡 Jeder Klick auf „Ausführen" oder „Prüfen" startet deinen Code in einem frischen, leeren
> Spielfeld – frühere Zeichnungen sind dann weg. Das ist Absicht: so fängt jede Aufgabe sauber
> von vorne an. Deshalb steht in jeder Aufgabe dieses Kurses der **komplette** Code für die
> Szene, nicht nur der neue Teil – kopiere bestehenden Code also nicht weg, sondern baue direkt
> darin weiter.
