# Example 2: Spaceship from geometric shapes
import turtle

screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Spaceship Design")

pen = turtle.Turtle()
pen.speed(5)
pen.color("cyan")

def draw_spaceship(x, y):
    pen.penup()
    pen.goto(x, y)
    pen.pendown()
    pen.fillcolor("silver")
    pen.begin_fill()
    # Main hull (elongated hexagon shape)
    pen.forward(60)
    pen.right(60)
    pen.forward(40)
    pen.right(120)
    pen.forward(40)
    pen.right(60)
    pen.forward(60)
    pen.right(60)
    pen.forward(40)
    pen.right(120)
    pen.forward(40)
    pen.right(60)
    pen.end_fill()
    # Cockpit window
    pen.penup()
    pen.goto(x + 30, y + 10)
    pen.fillcolor("cyan")
    pen.begin_fill()
    pen.circle(10)
    pen.end_fill()

draw_spaceship(-30, -20)

turtle.done()