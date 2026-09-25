# 📖 KI-Wortschatz

Ab jetzt begegnen dir immer wieder dieselben vier Begriffe. Merk sie dir gut, du brauchst sie den
ganzen Kurs über:

- **Trainingsdaten** – die Beispiele, aus denen der Computer lernt (z.B. deine `beispiele`-Liste
  aus der letzten Lektion)
- **Label** – die richtige Antwort zu jedem Beispiel (bei `("katze", "Säugetier")` ist
  `"Säugetier"` das Label)
- **Modell** – das, was am Ende aus den Trainingsdaten entsteht und für neue Eingaben eine
  Antwort liefert
- **Vorhersage** – die Antwort, die das Modell für eine neue, noch nicht bekannte Eingabe abgibt

Ein Dictionary kann schon als ganz einfaches Modell dienen:

```python
modell = {
    "apfel": "Obst",
    "karotte": "Gemüse",
    "kirsche": "Obst",
}

eingabe = "apfel"
vorhersage = modell.get(eingabe, "unbekannt")
print(vorhersage)

eingabe2 = "brot"
vorhersage2 = modell.get(eingabe2, "unbekannt")
print(vorhersage2)
```

`modell.get(eingabe, "unbekannt")` schaut nach, ob `eingabe` im Dictionary vorkommt – wenn nicht,
gibt es `"unbekannt"` zurück, statt abzustürzen.
