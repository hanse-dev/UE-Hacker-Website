import turtle

t = turtle.Turtle(); t.speed(10)
screen = turtle.Screen()
screen.bgcolor("black")

def rakete(x, y, groesse, farbe):
    t.penup(); t.goto(x, y); t.pendown()
    t.fillcolor(farbe); t.begin_fill()
    t.goto(x + groesse//2, y + groesse)
    t.goto(x + groesse, y)
    t.goto(x, y)
    t.end_fill()
    t.penup(); t.goto(x + groesse//2 - 3, y - groesse//3)
    t.fillcolor("orange"); t.begin_fill(); t.circle(groesse//6); t.end_fill()

def stern_logo(x, y, groesse, farbe):
    t.penup(); t.goto(x, y); t.pendown()
    t.fillcolor(farbe); t.begin_fill()
    for _ in range(5):
        t.forward(groesse); t.right(144)
    t.end_fill()

# Logo zusammensetzen
stern_logo(0, -60, 80, "gold")
stern_logo(0, -40, 50, "white")
rakete(-15, -20, 30, "silver")

t.penup(); t.goto(-80, 60)
t.color("cyan"); t.write("STERNENFLOTTE", font=("Arial", 12, "bold"))
t.goto(-60, 40); t.write("Interstellar Corps", font=("Arial", 9, "normal"))
t.hideturtle(); turtle.done()