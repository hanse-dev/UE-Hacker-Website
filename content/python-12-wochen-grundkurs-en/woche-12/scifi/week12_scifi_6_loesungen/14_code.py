import turtle

t = turtle.Turtle()
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Solar System"); t.speed(0)

def planet(orbit_radius, size, colour, name):
    # Orbit
    t.penup(); t.goto(0, -orbit_radius); t.pendown()
    t.color("gray"); t.circle(orbit_radius)
    # Planet
    t.penup(); t.goto(orbit_radius, 0)
    t.dot(size, colour)
    t.goto(orbit_radius + size, 8)
    t.color("white"); t.write(name, font=("Arial", 7, "normal"))

# Sun
t.penup(); t.goto(0, -20); t.dot(40, "yellow")

# Planets
planets = [
    (60, 8, "gray", "Mercury"),
    (90, 10, "orange", "Venus"),
    (120, 11, "blue", "Earth"),
    (160, 9, "red", "Mars"),
    (210, 20, "brown", "Jupiter"),
    (270, 17, "goldenrod", "Saturn"),
    (320, 13, "lightblue", "Uranus"),
    (360, 12, "blue", "Neptune"),
]
for args in planets:
    planet(*args)

t.hideturtle(); turtle.done()