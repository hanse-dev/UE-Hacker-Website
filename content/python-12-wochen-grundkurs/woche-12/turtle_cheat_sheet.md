# 🐢 Turtle Grafik Cheat Sheet

Willkommen zum ultimativen Turtle-Befehl Übersicht! Hier findest du alle wichtigen Befehle für deine grafischen Projekte.

## 📋 Grundlagen

### Import und Setup
```python
import turtle  # Turtle-Modul importieren

# Bildschirm einrichten
screen = turtle.Screen()
screen.title("Mein Turtle-Projekt")
screen.bgcolor("black")
screen.setup(800, 600)  # Breite, Höhe

# Turtle erstellen
pen = turtle.Turtle()
pen.speed(5)  # 1=langsam, 10=schnell, 0=sofort
```

### Programm beenden
```python
turtle.done()  # Wichtig am Ende!
```

## 🎨 Bewegungsbefehle

### Vorwärts und Rückwärts
```python
pen.forward(100)      # 100 Pixel vorwärts
pen.backward(50)      # 50 Pixel rückwärts
pen.fd(100)          # Kurzform für forward
pen.bk(50)           # Kurzform für backward
```

### Drehen
```python
pen.left(90)         # 90 Grad links drehen
pen.right(45)        # 45 Grad rechts drehen
pen.lt(90)           # Kurzform für left
pen.rt(45)           # Kurzform für right

# Zu absolutem Winkel drehen
pen.setheading(0)    # Nach Osten ausrichten
pen.setheading(90)   # Nach Norden ausrichten
pen.setheading(180)  # Nach Westen ausrichten
pen.setheading(270)  # Nach Süden ausrichten
```

### Positionierung
```python
pen.goto(100, 50)    # Zu Koordinate (x, y) bewegen
pen.setx(100)        # Nur X-Position ändern
pen.sety(50)         # Nur Y-Position ändern
pen.home()           # Zurück zum Startpunkt (0, 0)
```

## ✏️ Stift-Steuerung

### Stift hoch/runter
```python
pen.penup()          # Stift anheben (nicht zeichnen)
pen.pendown()        # Stift senken (zeichnen)
pen.up()             # Kurzform für penup
pen.down()           # Kurzform für pendown
```

### Stift-Status
```python
pen.isdown()         # True wenn Stift unten
pen.isup()           # True wenn Stift oben
```

## 🎨 Farben und Füllung

### Farben setzen
```python
pen.color("red")                     # Stiftfarbe
pen.color("red", "blue")             # Stiftfarbe, Füllfarbe
pen.pencolor("green")                # Nur Stiftfarbe
pen.fillcolor("yellow")              # Nur Füllfarbe

# RGB-Farben (0-255)
pen.pencolor(255, 0, 0)              # Rot
pen.fillcolor(0, 255, 0)             # Grün
```

### Füllungen
```python
pen.begin_fill()                     # Füllung starten
# Zeichne deine Form hier
pen.end_fill()                       # Füllung beenden

# Füll-Status
pen.filling()                        # True wenn gerade gefüllt wird
```

### Hintergrundfarbe
```python
screen.bgcolor("lightblue")          # Hintergrundfarbe ändern
```

## 📏 Linien-Eigenschaften

### Linienstärke
```python
pen.pensize(5)                       # Linienbreite 5 Pixel
pen.width(3)                         # Alternative für pensize
```

### Linienstil
```python
pen.resizemode("user")               # Größenänderung erlauben
pen.turtlesize(2, 2)                 # Turtle-Größe (Breite, Höhe)
```

## 🔷 Formen zeichnen

### Kreis
```python
pen.circle(50)                       # Kreis mit Radius 50
pen.circle(50, 180)                  # Halbkreis (180 Grad)
pen.circle(50, steps=5)              # Fünfeck
```

### Punkt
```python
pen.dot(20, "red")                   # Punkt mit Größe 20 und Farbe
pen.dot()                            # Kleiner Standard-Punkt
```

### Polygon
```python
# Quadrat
for _ in range(4):
    pen.forward(100)
    pen.left(90)

# Dreieck
for _ in range(3):
    pen.forward(100)
    pen.left(120)

# Sechseck
for _ in range(6):
    pen.forward(100)
    pen.left(60)
```

## 🐢 Turtle-Aussehen

### Form ändern
```python
pen.shape("turtle")                  # Schildkröte
pen.shape("arrow")                   # Pfeil
pen.shape("circle")                  # Kreis
pen.shape("square")                  # Quadrat
pen.shape("triangle")                # Dreieck
pen.shape("classic")                 # Klassischer Pfeil
```

### Sichtbarkeit
```python
pen.hideturtle()                     # Turtle verstecken
pen.showturtle()                     # Turtle zeigen
pen.isvisible()                      # True wenn sichtbar
```

## 📝 Text schreiben

### Text ausgeben
```python
pen.write("Hallo Welt!", font=("Arial", 16, "normal"))
pen.write("Python", font=("Times", 20, "bold"))
pen.write("Turtle", font=("Courier", 14, "italic"))
```

### Text-Positionierung
```python
pen.write("Text", align="center")    # Zentriert
pen.write("Text", align="right")     # Rechtsbündig
pen.write("Text", align="left")      # Linksbündig (Standard)
```

## 🔄 Zustand speichern

### Aktuellen Zustand speichern
```python
position = pen.position()            # Aktuelle Position
heading = pen.heading()              # Aktuelle Ausrichtung
```

### Zustand wiederherstellen
```python
pen.setposition(position)            # Position wiederherstellen
pen.setheading(heading)              # Ausrichtung wiederherstellen
```

## 🧹 Bildschirm steuern

### Bildschirm löschen
```python
pen.clear()                          # Nur Zeichnungen löschen
screen.clear()                       # Alles löschen
pen.reset()                          # Turtle zurücksetzen
```

### Bildschirm-Updates
```python
screen.tracer(0)                     # Animation aus
screen.update()                      # Manuell aktualisieren
screen.tracer(1)                     # Animation an (Standard)
```

## 🎯 Nützliche Funktionen

### Winkel berechnen
```python
import math
winkel = math.degrees(math.atan2(y2-y1, x2-x1))  # Winkel zwischen zwei Punkten
```

### Entfernung berechnen
```python
import math
distanz = math.sqrt((x2-x1)**2 + (y2-y1)**2)      # Entfernung zwischen zwei Punkten
```

### Zufällige Farben
```python
import random
zufallsfarbe = random.choice(["red", "blue", "green", "yellow"])
```

## 🎮 Animation Tipps

### Langsame Bewegung
```python
pen.speed(1)                         # Sehr langsam
pen.speed(3)                         # Langsam
pen.speed(5)                         # Normal
pen.speed(10)                        # Schnell
```

### Verzögerungen
```python
import time
time.sleep(1)                        # 1 Sekunde warten
```

### Bewegung glätten
```python
for i in range(100):
    pen.forward(1)
    pen.left(3.6)                    # Langsame Drehung
```

## 🐛 Fehlerbehebung

### Häufige Probleme
```python
# Problem: Nichts wird gezeichnet
# Lösung: pen.pendown() oder turtle.done() vergessen

# Problem: Turtle ist unsichtbar
# Lösung: pen.color("white") bei schwarzem Hintergrund

# Problem: Programm schließt sofort
# Lösung: turtle.done() am Ende hinzufügen
```

### Debug-Infos
```python
print(pen.position())               # Aktuelle Position ausgeben
print(pen.heading())                # Aktuelle Ausrichtung
print(pen.isdown())                 # Stift-Status prüfen
```

## 💡 Profi-Tipps

### Mehrere Turtles
```python
t1 = turtle.Turtle()
t2 = turtle.Turtle()
t1.color("red")
t2.color("blue")
```

### Funktionen für Formen
```python
def zeichne_quadrat(größe):
    for _ in range(4):
        pen.forward(größe)
        pen.left(90)

# Aufrufen
zeichne_quadrat(100)
```

### Koordinatensystem
```python
# Achsen zeichnen
pen.color("gray")
pen.goto(-300, 0)
pen.goto(300, 0)
pen.goto(0, -200)
pen.goto(0, 200)
```

## 🎨 Farb-Palette

### Standardfarben
- `"black"`, `"white"`, `"gray"`, `"red"`, `"green"`, `"blue"`
- `"yellow"`, `"orange"`, `"purple"`, `"pink"`, `"brown"`, `"cyan"`

### Spezielle Farben
- `"gold"`, `"silver"`, `"maroon"`, `"navy"`, `"olive"`, `"teal"`

### RGB-Farben
```python
# Pastellfarben
pen.pencolor(255, 182, 193)  # Hellrosa
pen.pencolor(176, 224, 230)  # Hellblau
pen.pencolor(152, 251, 152)  # Hellgrün

# Neonfarben
pen.pencolor(255, 0, 255)    # Magenta
pen.pencolor(0, 255, 255)    # Cyan
pen.pencolor(255, 255, 0)    # Gelb
```

---

## 🚀 Schnell-Referenz

| Kategorie | Befehl | Beispiel |
|----------|--------|---------|
| **Bewegung** | forward/backward | `pen.forward(100)` |
| | left/right | `pen.left(90)` |
| | goto | `pen.goto(50, 100)` |
| **Stift** | penup/pendown | `pen.penup()` |
| | color | `pen.color("red")` |
| | pensize | `pen.pensize(3)` |
| **Formen** | circle | `pen.circle(50)` |
| | dot | `pen.dot(20)` |
| | begin_fill/end_fill | `pen.begin_fill()` |
| **Text** | write | `pen.write("Hallo")` |
| **Zustand** | position | `pen.position()` |
| | heading | `pen.heading()` |
| | clear/reset | `pen.clear()` |

---

**Viel Spaß beim Zeichnen! 🎨**
