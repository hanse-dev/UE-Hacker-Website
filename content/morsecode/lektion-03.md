# Morse zurück in Text

Jetzt willst du die andere Richtung: aus Morsecode wieder lesbaren Text machen. Dafür brauchst du ein **umgekehrtes Dictionary** – eine Zuordnung von Morsezeichen zurück zu Buchstabe. Du musst es nicht von Hand neu eintippen: Python kann es aus dem bestehenden `MORSE`-Dictionary automatisch bauen:

```python
MORSE_UMGEKEHRT = {code: buchstabe for buchstabe, code in MORSE.items()}
```

Mit diesem umgekehrten Dictionary baust du jetzt die Rückrichtung. So läuft das Prinzip ab:

```
def aus_morse(code):
    zeichen_codes = code.split(" ")
    ergebnis = ""
    für jedes c in zeichen_codes:
        hänge MORSE_UMGEKEHRT[c] an ergebnis an
    gib ergebnis zurück
```

`code.split(" ")` zerlegt den Morsecode-String an jedem Leerzeichen wieder in seine einzelnen Zeichen-Codes. Rufst du z.B. `aus_morse(".... .")` auf, kommt `"he"` heraus.
