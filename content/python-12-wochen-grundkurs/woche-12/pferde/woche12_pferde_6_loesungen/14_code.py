import turtle, random

screen = turtle.Screen()
screen.bgcolor("lightblue")
screen.title("Pferderennen!")
screen.tracer(0)

farben = ["red", "blue", "green", "orange", "purple"]
pferde = []

for i, farbe in enumerate(farben):
    p = turtle.Turtle()
    p.shape("arrow"); p.color(farbe); p.penup()
    p.goto(-280, -80 + i * 40)
    pferde.append(p)

# Ziellinie
ziel = turtle.Turtle()
ziel.penup(); ziel.goto(250, -120); ziel.pendown()
ziel.goto(250, 120); ziel.hideturtle()

for runde in range(200):
    for pferd in pferde:
        pferd.forward(random.randint(1, 8))
    screen.update()
    sieger = [p for p in pferde if p.xcor() >= 250]
    if sieger:
        print(f"Sieger: Pferd {pferde.index(sieger[0])+1}!")
        break

turtle.done()