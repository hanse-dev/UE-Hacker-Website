# Antwort-Knöpfe erzeugen

Auf der Übungsfläche gibt es nur **einen** Knopf. Dein Quiz braucht aber für jede Antwort einen
eigenen. Die Lösung: Dein Code baut sich die fehlenden Knöpfe selbst.

Das geht in drei Schritten:

```js
const neuerKnopf = document.createElement('button'); // 1. Knopf erzeugen
neuerKnopf.textContent = 'Ich bin neu!';             // 2. beschriften
knopf.before(neuerKnopf);                            // 3. auf die Seite setzen
```

1. `document.createElement('button')` erzeugt einen neuen Knopf. Er existiert jetzt, ist aber noch
   **nirgends zu sehen**.
2. Mit `.textContent` bekommt er seine Beschriftung – genau wie bei den Elementen aus Woche 7.
3. Erst `knopf.before(neuerKnopf)` setzt ihn auf die Seite, und zwar direkt **vor** den Knopf, den
   es schon gibt.

Vergisst du Schritt 3, passiert scheinbar nichts: Der Knopf ist da, aber unsichtbar.

## Eine ID für jeden Knopf

Bisher hast du Elemente über ihre ID gefunden (`#knopf`, `#text`). Auch ein neues Element kann eine
ID bekommen:

```js
neuerKnopf.id = 'neu';
```

Für dein Quiz bekommen die Antwort-Knöpfe die IDs `antwort-0`, `antwort-1` und `antwort-2`. Die
Nummer am Ende passt genau zur Position der Antwort im Array.

## Mehrere Knöpfe mit einer Schleife

Für drei Antworten schreibst du nicht dreimal denselben Code, sondern nimmst eine `for`-Schleife.
In jedem Durchlauf entsteht ein neuer Knopf, und die Variable `i` hilft doppelt – beim Text
und bei der ID:

```
für i von 0 bis 2:
  erzeuge einen neuen Knopf
  Text des Knopfs = der i-te Eintrag aus dem Array
  ID des Knopfs = 'antwort-' + i
  setze den Knopf vor #knopf
```

`'antwort-' + i` hängt die Zahl an den Text: Aus `i = 2` wird `'antwort-2'`.

> 💡 Den alten Knopf brauchst du erst ganz am Ende des Projekts wieder. Bis dahin versteckst du
> ihn mit `knopf.hidden = true`. Er ist dann noch da, aber unsichtbar – mit `knopf.hidden = false`
> holst du ihn zurück.
