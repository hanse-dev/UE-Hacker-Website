import turtle, math

t = turtle.Turtle()
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Sonnensystem"); t.speed(0)

def planet(radius_bahn, groesse, farbe, name):
    # Umlaufbahn
    t.penup(); t.goto(0, -radius_bahn); t.pendown()
    t.color("gray"); t.circle(radius_bahn)
    # Planet
    t.penup(); t.goto(radius_bahn, 0)
    t.dot(groesse, farbe)
    t.goto(radius_bahn + groesse, 8)
    t.color("white"); t.write(name, font=("Arial", 7, "normal"))

# Sonne
t.penup(); t.goto(0, -20); t.dot(40, "yellow")

# Planeten
planeten = [
    (60, 8, "gray", "Merkur"),
    (90, 10, "orange", "Venus"),
    (120, 11, "blue", "Erde"),
    (160, 9, "red", "Mars"),
    (230, 20, "brown", "Jupiter"),
    (290, 17, "goldenrod", "Saturn"),
    (340, 13, "lightblue", "Uranus"),
    (380, 12, "blue", "Neptun"),
]
for args in planeten:
    planet(*args)

t.hideturtle(); turtle.done()