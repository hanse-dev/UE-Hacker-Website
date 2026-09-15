import turtle, random

screen = turtle.Screen()
screen.bgcolor("lightblue")
screen.title("Horse Race!")
screen.tracer(0)

colours = ["red", "blue", "green", "orange", "purple"]
horses = []

for i, colour in enumerate(colours):
    h = turtle.Turtle()
    h.shape("arrow")
    h.color(colour)
    h.penup()
    h.goto(-280, -80 + i * 40)
    horses.append(h)

finish = turtle.Turtle()
finish.penup()
finish.goto(250, -120)
finish.pendown()
finish.goto(250, 120)
finish.hideturtle()

for _ in range(200):
    for horse in horses:
        horse.forward(random.randint(1, 8))
    screen.update()
    winners = [h for h in horses if h.xcor() >= 250]
    if winners:
        print(f"Winner: Horse {horses.index(winners[0]) + 1}!")
        break

turtle.done()