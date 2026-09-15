import turtle

t = turtle.Turtle()
screen = turtle.Screen()
screen.bgcolor("lightgreen")
t.speed(8)

def draw_obstacle(x, y, height, number):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.color("brown")
    t.goto(x, y + height)
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.goto(x + 40, y + height)
    t.penup()
    t.goto(x + 40, y)
    t.pendown()
    t.goto(x + 40, y + height)
    t.penup()
    t.goto(x + 15, y + height + 5)
    t.write(str(number), font=("Arial", 10, "bold"))

for i in range(8):
    draw_obstacle(-300 + i * 80, -50, 30 + i * 5, i + 1)

t.hideturtle()
turtle.done()