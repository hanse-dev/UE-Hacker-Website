# Lehrplan – Python 12-Wochen-Grundkurs

Übersicht aller Konzepte pro Woche. Jede Woche hat drei parallele Kurse mit identischem Lerninhalt aber verschiedenen Themenrahmen (Abenteuer / Pferde / SciFi).

---

## Woche 1 – Grundlagen

**Neue Konzepte:**
- `print()` – Text auf dem Bildschirm ausgeben
- Variablen – Werte unter einem Namen speichern
- Datentypen (Überblick): `String`, `Integer`, `Boolean`
- String-Verkettung mit `+`
- `str()` – Zahl in Text umwandeln
- Kommentare mit `#`
- `input()` – erste Eingabe vom Benutzer einlesen

**Lernziele:** Einfache interaktive Programme schreiben, Variablen anlegen und ausgeben, erste Fehler finden und beheben.

---

## Woche 2 – Datentypen & Strings

**Neue Konzepte:**
- f-Strings – moderne Textzusammenstellung (`f"Hallo {name}"`)
- f-Strings vs. `+`-Verkettung – wann was benutzen
- `Float` – Kommazahlen
- `type()` – Datentyp einer Variable prüfen
- `len()` – Länge eines Textes ermitteln
- Typumwandlungen: `int()`, `float()`, `str()`, `bool()`
- String-Methoden: `.upper()`, `.lower()`, `.strip()`, `.split()`, `.replace()`
- `input()` vertiefen – Eingaben in andere Typen umwandeln (`int(input(...))`)

**Vertiefung:** Variablen (aus Woche 1), String und Integer

**Lernziele:** Alle vier Grundtypen kennen und umwandeln, Texte bearbeiten, Programme mit Benutzereingabe schreiben.

---

## Woche 3 – Bedingungen

**Neue Konzepte:**
- `if`, `elif`, `else` – Entscheidungen treffen
- Vergleichsoperatoren: `==`, `!=`, `<`, `>`, `<=`, `>=`
- Logische Operatoren: `and`, `or`, `not`

**Vertiefung:** Variablen, Datentypen, f-Strings, `input()`

**Lernziele:** Programme mit Fallunterscheidungen schreiben, Benutzereingaben prüfen.

---

## Woche 4 – Schleifen & Listen-Grundlagen

**Neue Konzepte:**

- `for`-Schleife – über eine Sammlung iterieren (`for item in liste`)
- `range()` – Zahlenfolge erzeugen (`for i in range(10)`)
- `while`-Schleife – solange wiederholen wie eine Bedingung gilt
- Listen `[]` – Grundlagen: erstellen, Elemente hinzufügen (`append()`), per Index zugreifen

**Vertiefung:** Bedingungen, Variablen

> 💡 Listen werden hier nur als Grundlage für sinnvolle `for`-Schleifen eingeführt.
> Alle Listen-Methoden kommen in Woche 6.

**Lernziele:**  Wiederholende Aufgaben automatisieren, `for`-Schleifen über echte Sammlungen schreiben.

---

## Woche 5 – Funktionen

**Neue Konzepte:**
- `def` – eine Funktion definieren
- Parameter & Argumente
- `return` – Ergebnis zurückgeben
- Docstrings – Funktionen dokumentieren
- Namenskonventionen (`snake_case`)
- `try` / `except` – Fehler abfangen (Grundlagen)

**Vertiefung:** `len()`, `type()` (aus Woche 2) im Funktions-Kontext, Listen aus Woche 4

**Lernziele:** Wiederverwendbaren Code schreiben, Programme in Teilaufgaben aufteilen, einfache Fehlerbehandlung.

---

## Woche 6 – Listen (vollständig)

**Neue Konzepte:**

- Listen-Methoden: `insert()`, `remove()`, `pop()`, `index()`, `count()`
- `in` – prüfen ob Element in Liste vorhanden
- `sort()`, `sorted()`, `reverse()`
- `enumerate()` – Index und Wert gleichzeitig in einer Schleife
- `break` – Schleife vorzeitig beenden
- `continue` – aktuelle Runde überspringen
- `set` – Duplikate entfernen (kurze Einführung)

**Vertiefung:** Listen-Grundlagen (Woche 4), Schleifen, Funktionen

> 💡 **Foreshadowing OOP:** Methoden wie `.append()` oder `.sort()` sind ein erstes Beispiel
> für OOP – die Liste ist ein Objekt, und diese Methoden gehören zu ihr. In Woche 10 bauen
> wir eigene Objekte mit eigenen Methoden.

**Lernziele:** Sammlungen vollständig verwalten, Listen durchsuchen und sortieren, Schleifen fein steuern.

---

## Woche 7 – Module & Bibliotheken

**Neue Konzepte:**
- `import` – Module laden
- `from … import …` und `import … as …`
- `math` – mathematische Funktionen (`sqrt`, `floor`, `ceil`, `pi`)
- `random` – Zufallszahlen (`randint`, `choice`, `shuffle`)

**Vertiefung:** Funktionen, Listen, Datentypen

> 💡 JSON wird hier bewusst ausgelassen – es wird in Woche 9 zusammen mit
> Datei-I/O eingeführt, wo es sinnvoll eingebettet ist.

**Lernziele:** Vorhandene Bibliotheken nutzen, Zufallselemente einbauen.

---

## Woche 8 – Dictionaries & Tupel

**Neue Konzepte:**
- Dictionaries `{}` – Schlüssel-Wert-Paare
- Zugriff mit `[]` und `.get()`
- Einträge hinzufügen, ändern, löschen (`.pop()`, `.update()`)
- Iteration: `.keys()`, `.values()`, `.items()`
- Tupel `()` – unveränderliche geordnete Sammlung
- Tupel-Unpacking

**Vertiefung:** Listen, Schleifen, Funktionen

> 💡 **Foreshadowing OOP:** Ein Dictionary mit festen Feldern (`{"name": "Aria", "level": 5}`)
> ist der Vorläufer einer Klasse. In Woche 10 ersetzen wir solche Dictionaries durch echte Objekte.

**Lernziele:** Strukturierte Daten mit benannten Feldern verwalten.

---

## Woche 9 – Dateien & I/O

**Neue Konzepte:**
- `open()` und `with` – Dateien öffnen und schließen
- Lesen und Schreiben von Textdateien
- `json` – JSON-Dateien lesen (`json.load`) und schreiben (`json.dump`)
- CSV-Dateien lesen (`csv.reader`) und schreiben (`csv.writer`)
- `try` / `except` für Dateifehler (`FileNotFoundError`)

**Vertiefung:** Dictionaries, Listen, try/except (aus Woche 5)

**Lernziele:** Daten dauerhaft speichern und einlesen.

---

## Woche 10 – OOP Grundlagen

**Neue Konzepte:**
- `class` – eine eigene Klasse definieren
- `__init__` – Konstruktor / Initialisierung
- `self` – Verweis auf die eigene Instanz
- Attribute – Eigenschaften eines Objekts
- Methoden – Funktionen eines Objekts
- Instanzen erstellen

**Vertiefung:** Funktionen, Dictionaries

> 💡 Brücke bauen: *"Erinnerst du dich an das Held-Dictionary aus Woche 8?
> Jetzt bauen wir daraus eine richtige Held-Klasse."*

**Lernziele:** Eigene Datenstrukturen mit Verhalten modellieren.

---

## Woche 11 – OOP Fortgeschritten

**Neue Konzepte:**
- Vererbung – eine Klasse von einer anderen ableiten
- `super()` – auf die Elternklasse zugreifen
- Polymorphismus – gleiche Methode, unterschiedliches Verhalten
- Magic Methods: `__str__`, `__repr__`, `__add__`, `__len__`, `__eq__`

**Vertiefung:** OOP Grundlagen (Woche 10)

**Lernziele:** Klassenhierarchien bauen, Objekte vergleichen und ausgeben.

---

## Woche 12 – Abschlussprojekt: Text-Adventure

**Keine neuen Grundkonzepte** – Woche 12 wendet alles aus Woche 1–11 in einem Projekt an:
- Spielwelt als verschachteltes Dictionary (Woche 8)
- Bewegung mit Funktionen, Bedingungen und Schleifen (Woche 3–5)
- Inventar als Liste, Klassen `Spieler`, `Gegenstand`, `Gegner` (Woche 6, 10, 11)
- Kämpfe mit `random` (Woche 7)
- Falsche Eingaben mit `try`/`except` abfangen (Woche 8)
- Spielstand speichern und laden mit JSON (Woche 9)

**Einziger neuer Begriff:** Komposition ("hat ein") – ein Objekt enthält andere Objekte.

> 💡 **OOP-Verbindung:** Vererbung ("ist ein") aus Woche 11 und Komposition ("hat ein") ergänzen sich.
> Im Projekt kommt bewusst nur Komposition vor.

**Lernziele:** Ein komplettes, mehrteiliges Programm planen und aus den Bausteinen des Kurses zusammensetzen.

---

## Nicht im Kurs enthalten (bewusste Auslassung)

Folgende Themen sind für einen Grundkurs zu fortgeschritten und werden nicht gelehrt:

- List Comprehensions
- Decorators / `@property`
- Abstrakte Klassen (`abc.ABC`, `@abstractmethod`)
- Generatoren und Iteratoren
- Type Hints (`typing`)
- `os`, `shutil`, `pathlib`
- Reguläre Ausdrücke
- Virtuelle Umgebungen / Package Management
- Testing-Frameworks
