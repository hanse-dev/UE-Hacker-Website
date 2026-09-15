import turtle, math

t = turtle.Turtle()
screen = turtle.Screen()
screen.bgcolor("white")
t.speed(10)

def stern(x, y, groesse, farbe):
    t.penup(); t.goto(x, y - groesse); t.pendown()
    t.fillcolor(farbe); t.begin_fill()
    for _ in range(5):
        t.forward(groesse); t.right(144)
    t.end_fill()

def kreis(x, y, radius, farbe):
    t.penup(); t.goto(x, y - radius); t.pendown()
    t.fillcolor(farbe); t.begin_fill()
    t.circle(radius)
    t.end_fill()

# Logo: äußerer Ring + Stern + Hufeisen-Text
kreis(0, 0, 100, "gold")
kreis(0, 0, 80, "white")
stern(0, 10, 60, "darkblue")

t.penup(); t.goto(-60, -90)
t.color("darkblue")
t.write("SONNENTAL CUP", font=("Arial", 11, "bold"))

t.hideturtle(); turtle.done()