import turtle, random

t = turtle.Turtle(); t.speed(0)
screen = turtle.Screen()
screen.bgcolor("black")

# Sterne
t.color("white")
for _ in range(150):
    x = random.randint(-380, 380)
    y = random.randint(-280, 280)
    t.penup(); t.goto(x, y); t.dot(random.choice([1, 2]))

# Sternsysteme
systeme = [
    (-200, 100, "Andromeda", "cyan", 30),
    (100, 150, "Kepler", "yellow", 25),
    (200, -80, "Proxima", "red", 20),
    (-100, -150, "Gliese", "orange", 22),
]
for x, y, name, farbe, radius in systeme:
    t.penup(); t.goto(x, y - radius)
    t.color(farbe); t.pendown(); t.circle(radius)
    t.penup(); t.goto(x - 30, y - radius - 15)
    t.color("white"); t.write(name, font=("Arial", 8, "normal"))

t.penup(); t.goto(-120, 200)
t.write("🌌 Bekannte Galaxien-Karte 🌌", font=("Arial", 12, "bold"))
t.hideturtle(); turtle.done()