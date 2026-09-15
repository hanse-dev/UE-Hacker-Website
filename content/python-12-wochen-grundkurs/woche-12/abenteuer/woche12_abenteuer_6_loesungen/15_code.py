# Lösungsvorschlag Mission 3 – Das magische Mandala
import turtle

screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Magisches Mandala")

stift = turtle.Turtle()
stift.speed(0)   # Schnellste Geschwindigkeit

farben = ["gold", "orange", "red", "purple", "blue", "cyan", "green", "lime"]

# Schritt 1 & 2: 8 symmetrische Teile
for i in range(8):
    stift.color(farben[i])

    # Äußerer Kreis
    stift.circle(80)

    # Inneres Dreieck
    for _ in range(3):
        stift.forward(60)
        stift.left(120)

    # Drehen für Symmetrie
    stift.right(360 / 8)

# Schritt 3: Zentraler Punkt
stift.penup()
stift.goto(0, -10)
stift.pendown()
stift.color("white")
stift.fillcolor("white")
stift.begin_fill()
stift.circle(10)
stift.end_fill()

# Titel
stift.penup()
stift.goto(0, -160)
stift.color("gold")
stift.write("✨ Magisches Mandala ✨", align="center", font=("Arial", 13, "bold"))

stift.hideturtle()
turtle.done()