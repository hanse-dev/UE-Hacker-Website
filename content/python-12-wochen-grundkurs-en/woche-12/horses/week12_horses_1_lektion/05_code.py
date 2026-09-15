# Example 2: Drawing obstacles
import turtle

screen = turtle.Screen()
screen.bgcolor("lightgreen")

obstacle_pen = turtle.Turtle()
obstacle_pen.speed(3)
obstacle_pen.color("brown")

def draw_obstacle(x, y, height):
    obstacle_pen.penup()
    obstacle_pen.goto(x, y)
    obstacle_pen.pendown()
    obstacle_pen.begin_fill()
    obstacle_pen.fillcolor("saddlebrown")
    for _ in range(2):
        obstacle_pen.forward(40)
        obstacle_pen.left(90)
        obstacle_pen.forward(height)
        obstacle_pen.left(90)
    obstacle_pen.end_fill()

draw_obstacle(-150, -100, 60)
draw_obstacle(-50, -100, 80)
draw_obstacle(50, -100, 70)
draw_obstacle(150, -100, 90)

turtle.done()