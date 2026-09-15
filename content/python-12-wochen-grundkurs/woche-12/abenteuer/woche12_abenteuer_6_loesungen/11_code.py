# Lösungsvorschlag Mission 1 – Die magische Rune zeichnen
import turtle

# Schritt 1: Fenster und Pentagramm
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Magische Rune")

rune = turtle.Turtle()
rune.speed(3)
rune.color("gold")
rune.fillcolor("darkgoldenrod")

# Pentagramm zeichnen
rune.begin_fill()
for _ in range(5):
    rune.forward(150)
    rune.right(144)
rune.end_fill()

# Schritt 2: Kreis um den Stern
rune.penup()
rune.goto(0, -120)   # Unterrand des Kreises
rune.pendown()
rune.color("silver")
rune.circle(120)

# Schritt 3: Runenzeichen als kleiner Text (Bonus)
rune.penup()
rune.goto(0, -160)
rune.color("white")
rune.write("✦ PYRALIA RUNE ✦", align="center", font=("Arial", 12, "bold"))

rune.hideturtle()
turtle.done()