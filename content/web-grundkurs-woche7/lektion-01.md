# Flex-Container

**Flexbox** ordnet Elemente in einer **Reihe** oder **Spalte** an. Du schaltest es am **Eltern**element ein – dem **Flex-Container**. Seine direkten Kinder heißen **Flex-Items**.

```css
.menue {
  display: flex;
  flex-direction: row;   /* Reihe – Standard */
  gap: 12px;             /* Abstand zwischen den Items */
}
```

| flex-direction | Anordnung |
|---|---|
| `row` | nebeneinander, von links nach rechts |
| `column` | untereinander |
| `row-reverse` / `column-reverse` | in umgekehrter Reihenfolge |

Die Richtung legt die **Hauptachse** fest. Quer dazu liegt die **Querachse** – das ist gleich beim Ausrichten wichtig.

> 💡 `display: flex` gehört an den **Container**, nicht an die Items. Ein häufiger Fehler!
