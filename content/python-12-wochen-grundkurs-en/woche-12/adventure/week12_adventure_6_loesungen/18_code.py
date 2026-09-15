import turtle

screen = turtle.Screen()
screen.bgcolor("lightgreen")
screen.title("Map of Pyralia")

map_pen = turtle.Turtle()
map_pen.speed(0)

def draw_border(pen):
    pen.penup()
    pen.goto(-280, -200)
    pen.pendown()
    pen.color("brown")
    pen.width(4)
    for _ in range(2):
        pen.forward(560)
        pen.left(90)
        pen.forward(400)
        pen.left(90)
    pen.width(1)

def draw_location(pen, x, y, colour, name):
    pen.penup()
    pen.goto(x, y - 15)
    pen.pendown()
    pen.color(colour)
    pen.fillcolor(colour)
    pen.begin_fill()
    pen.circle(15)
    pen.end_fill()
    pen.penup()
    pen.goto(x, y - 35)
    pen.color("black")
    pen.write(name, align="center", font=("Arial", 9, "bold"))

def draw_road(pen, x1, y1, x2, y2):
    pen.penup()
    pen.goto(x1, y1)
    pen.pendown()
    pen.color("sienna")
    pen.width(2)
    pen.goto(x2, y2)
    pen.width(1)

draw_border(map_pen)

locations = [
    (-150, 80, "royalblue", "Crystal Lake"),
    (100, 100, "darkgreen", "Magic Forest"),
    (0, -80, "gray", "Dragon Mountain"),
    (-100, -120, "gold", "Gold City")
]
for x, y, colour, name in locations:
    draw_location(map_pen, x, y, colour, name)

draw_road(map_pen, -150, 80, 100, 100)
draw_road(map_pen, 100, 100, 0, -80)
draw_road(map_pen, 0, -80, -100, -120)
draw_road(map_pen, -100, -120, -150, 80)

map_pen.penup()
map_pen.goto(210, 130)
map_pen.color("black")
map_pen.write("N", align="center", font=("Arial", 12, "bold"))
map_pen.goto(210, 90)
map_pen.write("S", align="center", font=("Arial", 12, "bold"))
map_pen.goto(230, 110)
map_pen.write("E", align="center", font=("Arial", 12, "bold"))
map_pen.goto(190, 110)
map_pen.write("W", align="center", font=("Arial", 12, "bold"))

map_pen.hideturtle()
turtle.done()