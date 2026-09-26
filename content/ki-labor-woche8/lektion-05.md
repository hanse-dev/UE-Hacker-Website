# 🤖 Grenzen von KI: Chatbots und Datenschutz

## Was macht ein Chatbot wie ChatGPT anders?

Alle Modelle dieses Kurses haben eines gemeinsam: Sie brauchen **von Menschen beschriftete**
Trainingsdaten (ein Label-Feld wie `"dringend"` oder `"schirm"`) und lösen genau **eine** enge
Aufgabe. Ein Chatbot wirkt dagegen, als würde er "alles verstehen". Der Kern-Trick dahinter ist
trotzdem verwandt: **das nächste Wort vorhersagen**, trainiert an riesigen Mengen unbeschrifteten
Textes (Bücher, Webseiten, …) – niemand hat "richtig"/"falsch" von Hand markiert.

```python
def naechste_woerter(texte, wort):
    kandidaten = {}
    for satz in texte:
        for i in range(len(satz) - 1):
            if satz[i] == wort:
                naechstes = satz[i + 1]
                kandidaten[naechstes] = kandidaten.get(naechstes, 0) + 1
    return kandidaten
```

Das ist eine **stark vereinfachte** Miniatur-Version desselben Grundprinzips: Wörter, die im
Trainingstext oft aufeinander folgen, werden als wahrscheinliche Fortsetzung gelernt – ganz ohne
Label. Echte Sprachmodelle tun das mit Milliarden Wörtern und viel größeren, tiefer verschachtelten
neuronalen Netzen, als du in Woche 6/7 selbst gebaut hast – aber sie haben kein echtes Verständnis
der Welt, sondern erkennen sehr gute statistische Muster. Und: weil sie aus echten Texten lernen,
übernehmen sie auch **Bias**, der in diesen Texten steckt – aus genau dem Grund, den du diese
Woche am Entscheidungsbaum gesehen hast.

## Datenschutz

KI-Systeme brauchen Daten – oft auch **personenbezogene** Daten (Name, E-Mail, Standort, Verhalten
in einer App). Das ist heikel: Diese Daten könnten weitergegeben, gehackt oder für andere Zwecke
genutzt werden, als wofür sie gesammelt wurden. Eine einfache Schutzmaßnahme ist
**Anonymisierung**: identifizierende Felder entfernen oder verallgemeinern, bevor Daten
gespeichert oder ausgewertet werden.

```python
def anonymisiere(profil):
    return {
        "name": None,
        "email": None,
        "alter": profil["alter"],
        "plz": profil["plz"],
    }
```

Wichtig zu wissen: Anonymisierung ist **kein Allheilmittel**. Selbst ohne Namen kann eine seltene
Kombination aus Merkmalen (z.B. eine bestimmte Postleitzahl **und** ein genaues Alter) eine Person
trotzdem eindeutig identifizierbar machen – das siehst du in einer der Extra-Herausforderungen
dieser Woche.
