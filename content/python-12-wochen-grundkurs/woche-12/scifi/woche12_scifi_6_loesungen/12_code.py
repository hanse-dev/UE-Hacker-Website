import turtle

t = turtle.Turtle()
screen = turtle.Screen()
screen.bgcolor("black")
t.speed(10); t.color("silver")

def zeichne_schiff(x, y, groesse):
    t.penup(); t.goto(x, y); t.pendown()
    t.fillcolor("gray"); t.begin_fill()
    # Dreieck als Schiff
    t.goto(x + groesse, y + groesse // 2)
    t.goto(x, y + groesse)
    t.goto(x - groesse // 3, y + groesse // 2)
    t.goto(x, y)
    t.end_fill()
    # Triebwerk
    t.penup(); t.goto(x - groesse // 3, y + groesse // 2)
    t.color("orange"); t.dot(groesse // 4)
    t.color("silver")

# V-Formation
positionen = [
    (0, 50, 25),
    (-60, 0, 20), (60, 0, 20),
    (-120, -50, 15), (120, -50, 15),
]
for x, y, g in positionen:
    zeichne_schiff(x, y, g)

t.penup(); t.goto(-80, 120)
t.color("white"); t.write("Flottenformation Alpha", font=("Arial", 11, "bold"))
t.hideturtle(); turtle.done()