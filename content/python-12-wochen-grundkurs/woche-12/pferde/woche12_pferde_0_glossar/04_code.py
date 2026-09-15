import turtle

t = turtle.Turtle()
t.speed(5)

# Quadrat zeichnen
for _ in range(4):
    t.forward(100)
    t.right(90)

# Farbiger Kreis
t.penup()
t.goto(0, -50)
t.pendown()
t.color("blue")
t.fillcolor("lightblue")
t.begin_fill()
t.circle(50)
t.end_fill()

turtle.done()
