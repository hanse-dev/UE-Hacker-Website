import turtle

t = turtle.Turtle()
screen = turtle.Screen()
screen.bgcolor("green")
screen.title("Sonnental Riding School")
t.speed(8)

def draw_area(x, y, width, height, colour, label):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.fillcolor(colour)
    t.begin_fill()
    for _ in range(2):
        t.forward(width)
        t.left(90)
        t.forward(height)
        t.left(90)
    t.end_fill()
    t.penup()
    t.goto(x + width / 2, y + height / 2 - 8)
    t.write(label, align="center", font=("Arial", 9, "bold"))

draw_area(-250, 50, 120, 80, "brown", "Stable")
draw_area(-100, 30, 150, 100, "lightblue", "Arena")
draw_area(80, 50, 120, 80, "lightgreen", "Pasture")
draw_area(-250, -120, 100, 60, "beige", "House")

t.hideturtle()
turtle.done()