# Beispiel 1: Turtle einrichten
import turtle

# Erstelle eine magische Zeichenrolle
screen = turtle.Screen()
screen.title("Magische Zeichenrolle von Pyralia")
screen.bgcolor("black")

# Erstelle einen magischen Stift (Turtle)
pen = turtle.Turtle()
pen.speed(1)  # Langsam für magische Effekte
pen.color("cyan")

# Zeichne eine magische Form
pen.forward(100)
pen.left(90)
pen.forward(100)

# Schließe die magische Zeichenrolle
turtle.done()