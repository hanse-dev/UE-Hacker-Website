import turtle

t = turtle.Turtle()
screen = turtle.Screen()
screen.bgcolor("green")
screen.title("Dressage Arena")
t.speed(6)

t.color("white")
t.pensize(3)
t.penup()
t.goto(-200, -100)
t.pendown()
for length in [400, 200, 400, 200]:
    t.forward(length)
    t.left(90)

positions = [(-200, -110, "C"), (195, -110, "M"), (195, 95, "A"), (-200, 95, "B")]
for x, y, letter in positions:
    t.penup()
    t.goto(x, y)
    t.write(letter, font=("Arial", 12, "bold"))

t.hideturtle()
turtle.done()