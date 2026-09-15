# Problem: Schwarze Sterne auf weißem Grund
import turtle

screen = turtle.Screen()
screen.bgcolor("black")  # Schwarzer Hintergrund

stern = turtle.Turtle()
stern.color("yellow")  # Gelbe Sterne
stern.begin_fill()
stern.fillcolor("white")  # Weiße Füllung
stern.circle(5)
stern.end_fill()
turtle.done()