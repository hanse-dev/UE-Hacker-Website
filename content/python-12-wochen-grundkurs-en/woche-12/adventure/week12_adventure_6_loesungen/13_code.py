import turtle

screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Wizard's Hat")

hat = turtle.Turtle()
hat.speed(3)

# Step 1: Hat body
hat.penup()
hat.goto(-50, -50)
hat.pendown()
hat.color("purple")
hat.fillcolor("purple")
hat.begin_fill()
for side in [100, 150, 100, 150]:
    hat.forward(side)
    hat.left(90)
hat.end_fill()

# Brim
hat.penup()
hat.goto(-80, -50)
hat.pendown()
hat.color("blue")
hat.fillcolor("blue")
hat.begin_fill()
for _ in range(2):
    hat.forward(160)
    hat.left(90)
    hat.forward(20)
    hat.left(90)
hat.end_fill()

# Star decoration
hat.penup()
hat.goto(10, 30)
hat.pendown()
hat.color("yellow")
hat.fillcolor("yellow")
hat.begin_fill()
for _ in range(5):
    hat.forward(20)
    hat.right(144)
hat.end_fill()

hat.penup()
hat.goto(0, -100)
hat.color("white")
hat.write("🌟 Wizard's Hat of Merlin", align="center", font=("Arial", 11, "bold"))

hat.hideturtle()
turtle.done()