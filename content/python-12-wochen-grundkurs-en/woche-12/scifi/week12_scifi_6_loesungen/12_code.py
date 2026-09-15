import turtle

t = turtle.Turtle()
screen = turtle.Screen()
screen.bgcolor("black")
t.speed(10); t.color("silver")

def draw_ship(x, y, size):
    t.penup(); t.goto(x, y); t.pendown()
    t.fillcolor("gray"); t.begin_fill()
    t.goto(x + size, y + size // 2)
    t.goto(x, y + size)
    t.goto(x - size // 3, y + size // 2)
    t.goto(x, y)
    t.end_fill()
    t.penup(); t.goto(x - size // 3, y + size // 2)
    t.color("orange"); t.dot(size // 4)
    t.color("silver")

# V-formation
positions = [
    (0, 50, 25),
    (-60, 0, 20), (60, 0, 20),
    (-120, -50, 15), (120, -50, 15),
]
for x, y, g in positions:
    draw_ship(x, y, g)

t.penup(); t.goto(-90, 120)
t.color("white"); t.write("Fleet Formation Alpha", font=("Arial", 11, "bold"))
t.hideturtle(); turtle.done()