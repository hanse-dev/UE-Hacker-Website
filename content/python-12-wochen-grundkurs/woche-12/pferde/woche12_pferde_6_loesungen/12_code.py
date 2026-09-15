import turtle

t = turtle.Turtle()
screen = turtle.Screen()
screen.bgcolor("lightgreen")
t.speed(8)

def zeichne_hindernis(x, y, hoehe, nummer):
    t.penup(); t.goto(x, y); t.pendown()
    t.color("brown")
    # Ständer links
    t.goto(x, y + hoehe)
    t.penup(); t.goto(x, y); t.pendown()
    # Stange
    t.goto(x + 40, y + hoehe)
    t.penup(); t.goto(x + 40, y); t.pendown()
    t.goto(x + 40, y + hoehe)
    # Nummer
    t.penup(); t.goto(x + 15, y + hoehe + 5)
    t.write(str(nummer), font=("Arial", 10, "bold"))

# 8 Hindernisse
for i in range(8):
    zeichne_hindernis(-300 + i * 80, -50, 30 + i * 5, i + 1)

t.hideturtle()
turtle.done()