import turtle, random

t = turtle.Turtle(); t.speed(0)
screen = turtle.Screen()
screen.bgcolor("black")

# Stars
t.color("white")
for _ in range(150):
    x = random.randint(-380, 380)
    y = random.randint(-280, 280)
    t.penup(); t.goto(x, y); t.dot(random.choice([1, 2]))

# Star systems
systems = [
    (-200, 100, "Andromeda", "cyan", 30),
    (100, 150, "Kepler", "yellow", 25),
    (200, -80, "Proxima", "red", 20),
    (-100, -150, "Gliese", "orange", 22),
]
for x, y, name, colour, radius in systems:
    t.penup(); t.goto(x, y - radius)
    t.color(colour); t.pendown(); t.circle(radius)
    t.penup(); t.goto(x - 30, y - radius - 15)
    t.color("white"); t.write(name, font=("Arial", 8, "normal"))

t.penup(); t.goto(-120, 200)
t.write("🌌 Known Galaxy Map 🌌", font=("Arial", 12, "bold"))
t.hideturtle(); turtle.done()