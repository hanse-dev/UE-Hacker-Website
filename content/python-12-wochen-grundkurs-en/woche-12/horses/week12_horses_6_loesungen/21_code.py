import turtle

t = turtle.Turtle()
screen = turtle.Screen()
screen.bgcolor("lightyellow")
t.speed(10)

def draw_horse(x, y, size, colour):
    t.penup()
    t.goto(x, y)
    t.fillcolor(colour)
    t.color("brown", colour)
    t.pendown()
    t.begin_fill()
    for _ in range(2):
        t.forward(size * 2)
        t.left(90)
        t.forward(size)
        t.left(90)
    t.end_fill()
    # Head
    t.penup()
    t.goto(x + size * 2, y + size * 0.7)
    t.begin_fill()
    t.circle(size * 0.4)
    t.end_fill()
    # Legs
    for leg_x in [x + 0.3 * size, x + 0.6 * size, x + 1.2 * size, x + 1.6 * size]:
        t.penup()
        t.goto(leg_x, y)
        t.pendown()
        t.goto(leg_x, y - size * 0.8)
    t.penup()
    t.goto(x + size, y - size - 10)
    t.color("black")
    t.write(colour.title(), align="center", font=("Arial", 8, "normal"))

draw_horse(-280, -20, 40, "brown")
draw_horse(-80, -20, 40, "gray")
draw_horse(120, -20, 40, "black")

t.penup()
t.goto(0, 90)
t.write("🐴 Horse Gallery 🐴", align="center", font=("Arial", 14, "bold"))
t.hideturtle()
turtle.done()