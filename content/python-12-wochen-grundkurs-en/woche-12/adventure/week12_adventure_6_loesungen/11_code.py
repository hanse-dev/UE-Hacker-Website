import turtle

screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Magic Rune")

rune = turtle.Turtle()
rune.speed(3)
rune.color("gold")
rune.fillcolor("darkgoldenrod")

# Draw pentagram
rune.begin_fill()
for _ in range(5):
    rune.forward(150)
    rune.right(144)
rune.end_fill()

# Circle around the star
rune.penup()
rune.goto(0, -120)
rune.pendown()
rune.color("silver")
rune.circle(120)

# Bonus: rune label
rune.penup()
rune.goto(0, -160)
rune.color("white")
rune.write("✦ PYRALIA RUNE ✦", align="center", font=("Arial", 12, "bold"))

rune.hideturtle()
turtle.done()