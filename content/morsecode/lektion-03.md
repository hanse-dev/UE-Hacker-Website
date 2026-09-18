# Morse zurück in Text

Jetzt willst du die andere Richtung: aus Morsecode wieder lesbaren Text machen. Dafür brauchst du ein **umgekehrtes Dictionary** – eine Zuordnung von Morsezeichen zurück zu Buchstabe. Du musst es nicht von Hand neu eintippen: Python kann es aus dem bestehenden `MORSE`-Dictionary automatisch bauen:

```python
MORSE_UMGEKEHRT = {code: buchstabe for buchstabe, code in MORSE.items()}

def aus_morse(code):
    zeichen_codes = code.split(" ")
    ergebnis = ""
    for c in zeichen_codes:
        ergebnis = ergebnis + MORSE_UMGEKEHRT[c]
    return ergebnis

print(aus_morse("... --- ..."))   # sos
```

`code.split(" ")` zerlegt den Morsecode-String an jedem Leerzeichen wieder in seine einzelnen Zeichen-Codes.
