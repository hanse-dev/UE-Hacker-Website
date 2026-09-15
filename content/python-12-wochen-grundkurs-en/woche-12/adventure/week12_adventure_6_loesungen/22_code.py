import turtle
import random

screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Magic Random Art")

class MagicPainter:
    def __init__(self):
        self.pen = turtle.Turtle()
        self.pen.speed(0)
        self.pen.hideturtle()
        self.magic_colours = [
            "gold", "cyan", "magenta", "orange", "lime",
            "purple", "pink", "aquamarine", "tomato", "orchid"
        ]

    def draw_magic_star(self, x, y, size, colour):
        self.pen.penup()
        self.pen.goto(x, y)
        self.pen.pendown()
        self.pen.color(colour)
        self.pen.fillcolor(colour)
        self.pen.begin_fill()
        for _ in range(5):
            self.pen.forward(size)
            self.pen.right(144)
        self.pen.end_fill()

    def draw_magic_circle(self, x, y, radius, colour):
        self.pen.penup()
        self.pen.goto(x, y - radius)
        self.pen.pendown()
        self.pen.color(colour)
        self.pen.fillcolor(colour)
        self.pen.begin_fill()
        self.pen.circle(radius)
        self.pen.end_fill()

    def draw_spiral(self, x, y, colour):
        self.pen.penup()
        self.pen.goto(x, y)
        self.pen.pendown()
        self.pen.color(colour)
        for i in range(20):
            self.pen.forward(i * 3)
            self.pen.right(45)

    def create_artwork(self, count=12):
        shapes = ["star", "circle", "spiral"]
        for _ in range(count):
            x = random.randint(-250, 250)
            y = random.randint(-180, 180)
            colour = random.choice(self.magic_colours)
            shape = random.choice(shapes)
            if shape == "star":
                size = random.randint(20, 60)
                self.draw_magic_star(x, y, size, colour)
            elif shape == "circle":
                radius = random.randint(10, 40)
                self.draw_magic_circle(x, y, radius, colour)
            else:
                self.draw_spiral(x, y, colour)

artist = MagicPainter()
artist.create_artwork(count=15)

artist.pen.penup()
artist.pen.goto(0, -215)
artist.pen.color("gold")
artist.pen.write("✨ Random Art by MagicPainter ✨", align="center", font=("Arial", 10, "italic"))

print()
print("🎉 Boss Quest completed!")
print("🏆 You have defeated the Master of the Drawing Scrolls!")
print("⭐ Title earned: Mage of the Visual Arts")
print()
print("🎊 CONGRATULATIONS! You have mastered Week 12!")

turtle.done()