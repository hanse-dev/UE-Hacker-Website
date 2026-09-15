import turtle

t = turtle.Turtle(); t.speed(10)
screen = turtle.Screen()
screen.bgcolor("black")

def draw_rocket(x, y, size, colour):
    t.penup(); t.goto(x, y); t.pendown()
    t.fillcolor(colour); t.begin_fill()
    t.goto(x + size // 2, y + size)
    t.goto(x + size, y)
    t.goto(x, y)
    t.end_fill()
    t.penup(); t.goto(x + size // 2 - 3, y - size // 3)
    t.fillcolor("orange"); t.begin_fill(); t.circle(size // 6); t.end_fill()

def draw_star_shape(x, y, size, colour):
    t.penup(); t.goto(x, y); t.pendown()
    t.fillcolor(colour); t.begin_fill()
    for _ in range(5):
        t.forward(size); t.right(144)
    t.end_fill()

draw_star_shape(0, -60, 80, "gold")
draw_star_shape(0, -40, 50, "white")
draw_rocket(-15, -20, 30, "silver")

t.penup(); t.goto(-80, 60)
t.color("cyan"); t.write("STARFLEET", font=("Arial", 12, "bold"))
t.goto(-60, 40); t.write("Interstellar Corps", font=("Arial", 9, "normal"))
t.hideturtle(); turtle.done()