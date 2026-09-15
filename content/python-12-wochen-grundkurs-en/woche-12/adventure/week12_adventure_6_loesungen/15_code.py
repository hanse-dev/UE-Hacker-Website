import turtle

screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Magic Mandala")

pen = turtle.Turtle()
pen.speed(0)

colours = ["gold", "orange", "red", "purple", "blue", "cyan", "green", "lime"]

for i in range(8):
    pen.color(colours[i])
    pen.circle(80)
    for _ in range(3):
        pen.forward(60)
        pen.left(120)
    pen.right(360 / 8)

# Central dot
pen.penup()
pen.goto(0, -10)
pen.pendown()
pen.color("white")
pen.fillcolor("white")
pen.begin_fill()
pen.circle(10)
pen.end_fill()

pen.penup()
pen.goto(0, -160)
pen.color("gold")
pen.write("✨ Magic Mandala ✨", align="center", font=("Arial", 13, "bold"))

pen.hideturtle()
turtle.done()