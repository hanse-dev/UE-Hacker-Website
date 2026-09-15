import turtle

t = turtle.Turtle()
screen = turtle.Screen()
screen.bgcolor("white")
t.speed(10)

def draw_star(x, y, size, colour):
    t.penup()
    t.goto(x, y - size)
    t.pendown()
    t.fillcolor(colour)
    t.begin_fill()
    for _ in range(5):
        t.forward(size)
        t.right(144)
    t.end_fill()

def draw_circle(x, y, radius, colour):
    t.penup()
    t.goto(x, y - radius)
    t.pendown()
    t.fillcolor(colour)
    t.begin_fill()
    t.circle(radius)
    t.end_fill()

draw_circle(0, 0, 100, "gold")
draw_circle(0, 0, 80, "white")
draw_star(0, 10, 60, "darkgreen")

t.penup()
t.goto(-70, -90)
t.color("darkgreen")
t.write("SONNENTAL CUP", font=("Arial", 11, "bold"))

t.hideturtle()
turtle.done()