import turtle

t = turtle.Turtle()
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Space Station Nebula-7")
t.speed(8)
t.color("white")

# Main ring
t.penup(); t.goto(0, -120); t.pendown()
t.circle(120)
t.penup(); t.goto(0, -80); t.pendown()
t.circle(80)

# Solar panels
for angle in [0, 90, 180, 270]:
    t.penup(); t.goto(0, 0); t.setheading(angle)
    t.forward(80); t.pendown()
    t.forward(60); t.left(90); t.forward(15)
    t.backward(30); t.right(90)
    t.backward(60)

# Docking ports
t.color("cyan")
for angle in [45, 135, 225, 315]:
    t.penup(); t.goto(0, 0); t.setheading(angle)
    t.forward(120); t.pendown(); t.dot(8)

t.penup(); t.goto(-60, 130)
t.write("NEBULA-7", font=("Arial", 12, "bold"))
t.hideturtle(); turtle.done()