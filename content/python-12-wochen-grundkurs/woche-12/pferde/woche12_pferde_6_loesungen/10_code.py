import turtle

t = turtle.Turtle()
screen = turtle.Screen()
screen.bgcolor("green")
screen.title("Dressur-Bahn")
t.speed(6)

# Reitplatz-Rechteck
t.color("white")
t.pensize(3)
t.penup(); t.goto(-200, -100); t.pendown()
for laenge in [400, 200, 400, 200]:
    t.forward(laenge); t.left(90)

# Buchstaben an den Ecken
t.penup()
positionen = [(-200, -110, "C"), (195, -110, "M"), (195, 95, "A"), (-200, 95, "B")]
for x, y, letter in positionen:
    t.goto(x, y)
    t.write(letter, font=("Arial", 12, "bold"))

t.hideturtle()
turtle.done()