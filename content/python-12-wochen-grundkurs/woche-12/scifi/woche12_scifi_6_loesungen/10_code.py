import turtle

t = turtle.Turtle()
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Raumstation Nebula-7")
t.speed(8); t.color("white")

# Hauptring
t.penup(); t.goto(0, -120); t.pendown()
t.circle(120)
t.penup(); t.goto(0, -80); t.pendown()
t.circle(80)

# Solarpaneele
for winkel in [0, 90, 180, 270]:
    t.penup(); t.goto(0, 0); t.setheading(winkel)
    t.forward(80); t.pendown()
    t.forward(60); t.left(90); t.forward(15)
    t.backward(30); t.right(90)
    t.backward(60)

# Andockstellen
t.color("cyan")
for winkel in [45, 135, 225, 315]:
    t.penup(); t.goto(0, 0); t.setheading(winkel)
    t.forward(120); t.pendown(); t.dot(8)

t.penup(); t.goto(-60, 130)
t.write("NEBULA-7", font=("Arial", 12, "bold"))
t.hideturtle(); turtle.done()