# Das Schlüsselwort wiederholen

Dein Text ist meistens länger als dein Schlüsselwort. Die Lösung: Das Schlüsselwort wird einfach so oft wiederholt, bis es genauso lang ist wie der Text.

Bei Text `"baum"` (4 Buchstaben) und Schlüsselwort `"ok"` (2 Buchstaben) sieht das so aus:

```
b a u m
o k o k
```

Um herauszufinden, welcher Schlüsselbuchstabe zu welcher Position im Text gehört, nutzt du den **Modulo-Operator** `%` – genau wie beim Wraparound in deiner Cäsar-Chiffre. So läuft das Prinzip ab:

```
schluesselwort = "ok"
position = 5
index = position modulo Länge von schluesselwort
buchstabe = schluesselwort an der Stelle index
```

`5 % 2` ergibt `1` – also den zweiten Buchstaben von `"ok"`. Egal wie lang der Text ist, `% len(schluesselwort)` sorgt dafür, dass der Index immer wieder von vorne beim Schlüsselwort anfängt.

> 💡 Modulo (`%`) und der Wraparound-Trick kommen direkt aus [Lektion 2 deines Cäsar-Chiffre-Projekts](/kurs/projekt-caesar-chiffre).
