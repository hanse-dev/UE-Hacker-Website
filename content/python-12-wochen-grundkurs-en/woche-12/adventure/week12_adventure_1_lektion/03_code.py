# Example 1: Setting up Turtle
import turtle

# Create a magic drawing scroll
screen = turtle.Screen()
screen.title("Magic Drawing Scroll of Pyralia")
screen.bgcolor("black")

# Create a magic pen (Turtle)
pen = turtle.Turtle()
pen.speed(1)  # Slow for magical effects
pen.color("cyan")

# Draw a magic shape
pen.forward(100)
pen.left(90)
pen.forward(100)

# Close the magic drawing scroll
turtle.done()