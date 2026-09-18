# Unbekannte Zeichen abfangen

Was passiert, wenn im Text ein Zeichen vorkommt, das gar nicht im `MORSE`-Dictionary steht – zum Beispiel ein Ausrufezeichen? `MORSE['!']` würde mit einem `KeyError` abstürzen, weil `'!'` kein Schlüssel im Dictionary ist.

Die Lösung: `.get(schluessel, ersatzwert)` statt `[schluessel]`. Damit bekommst du entweder den echten Wert – oder, falls der Schlüssel fehlt, einen Ersatzwert deiner Wahl, ohne Absturz:

```python
print(MORSE.get('a', '?'))   # .-   (a ist bekannt)
print(MORSE.get('!', '?'))   # ?    (! ist unbekannt, kein Absturz)
```

Baue jetzt eine robuste Version von `in_morse`, die `.get()` statt `[...]` benutzt, damit unbekannte Zeichen einfach zu `'?'` werden.
