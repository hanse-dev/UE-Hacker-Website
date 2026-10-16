# Platz verteilen

Bisher waren die Items so breit wie ihr Inhalt. Mit `flex` an einem **Item** darf es freien Platz aufnehmen:

```css
.spalte {
  flex: 1;
}
```

Haben alle Spalten `flex: 1`, teilen sie sich den Platz **gleichmäßig**. Bekommt eine `flex: 2`, wird sie doppelt so breit wie eine mit `flex: 1`.

Typisches Beispiel: eine Suchleiste, in der das Eingabefeld den Rest des Platzes füllt:

```css
.suche { display: flex; gap: 8px; }
.suche input { flex: 1; }
```

> 💡 `flex: 1` ist eine Kurzschreibweise. Der wichtigste Teil darin ist `flex-grow: 1` – „wachse mit, wenn Platz frei ist“.
