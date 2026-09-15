# Example 3: Planet system
import turtle

screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Nebula-7 Planetary System")

pen = turtle.Turtle()
pen.speed(0)
pen.hideturtle()

# Sun
pen.penup()
pen.goto(0, -50)
pen.fillcolor("orange")
pen.begin_fill()
pen.circle(50)
pen.end_fill()

# Planet 1
pen.penup()
pen.goto(120, -20)
pen.fillcolor("lightblue")
pen.begin_fill()
pen.circle(20)
pen.end_fill()

# Planet 2 with ring
pen.penup()
pen.goto(230, -30)
pen.fillcolor("tan")
pen.begin_fill()
pen.circle(30)
pen.end_fill()
# Ring
pen.penup()
pen.goto(230, -40)
pen.color("gray")
pen.pendown()
pen.width(4)
pen.circle(45)
pen.width(1)

turtle.done()