# Der komplette Übersetzer

Jetzt hast du alle Bausteine: Text → Morse und Morse → Text. Bau daraus ein einziges Werkzeug, das beide Richtungen kann – du sagst ihm nur, in welche Richtung es übersetzen soll:

```python
def uebersetze(text, richtung):
    if richtung == 'code':
        return in_morse_sicher(text)
    else:
        return aus_morse(text)
```

`uebersetze(..., 'code')` übersetzt Text in Morsecode, alles andere übersetzt Morsecode zurück in Text. Vervollständige die Funktion und probiere beide Richtungen aus.
