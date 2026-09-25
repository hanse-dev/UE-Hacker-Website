# Der komplette Übersetzer

Jetzt hast du alle Bausteine: Text → Morse und Morse → Text. Bau daraus ein einziges Werkzeug, das beide Richtungen kann – du sagst ihm nur, in welche Richtung es übersetzen soll. So läuft das Prinzip ab:

```
def uebersetze(text, richtung):
    wenn richtung gleich 'code' ist:
        gib in_morse_sicher(text) zurück
    sonst:
        gib aus_morse(text) zurück
```

`uebersetze(..., 'code')` übersetzt Text in Morsecode, alles andere übersetzt Morsecode zurück in Text. Vervollständige die Funktion und probiere beide Richtungen aus.
