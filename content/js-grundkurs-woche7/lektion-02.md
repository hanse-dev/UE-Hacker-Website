# Text verändern

Genauso wie du eine Property lesen kannst, kannst du sie auch **überschreiben** – dadurch ändert
sich sofort, was auf der Übungsfläche zu sehen ist:

```js
let ueberschrift = document.querySelector('#ueberschrift');
ueberschrift.textContent = 'Hallo JavaScript!';
```

Sobald diese Zeile läuft, zeigt die Überschrift rechts sofort den neuen Text – ganz ohne die Seite
neu zu laden. Das ist der Kern von "interaktivem" JavaScript: dein Code verändert direkt, was die
Nutzer:in sieht.

> 💡 Du kannst `document.querySelector(...)` auch direkt mit `.textContent = ...` in einer Zeile
> kombinieren, ohne den Umweg über eine eigene Variable:
> ```js
> document.querySelector('#ueberschrift').textContent = 'Hallo JavaScript!';
> ```
