# Umbrechen

Standardmäßig quetscht Flexbox **alle** Items in eine Zeile – auch wenn sie dabei winzig werden. Mit `flex-wrap` dürfen sie umbrechen:

```css
.galerie {
  display: flex;
  flex-wrap: wrap;
  gap: 12px;
}
.galerie img {
  width: 120px;
}
```

Ist eine Zeile voll, geht es in der nächsten weiter – wie bei Text. Genau so sind die meisten Bildergalerien gebaut.

> 💡 Mach die Vorschau schmaler oder breiter (zum Beispiel, indem du das Browserfenster änderst): Die Bilder ordnen sich neu an.
