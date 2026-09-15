import turtle

t = turtle.Turtle(); t.speed(10)
screen = turtle.Screen()
screen.bgcolor("black")

def draw_ship(x, y, size, colour, name):
    t.penup(); t.goto(x, y); t.pendown()
    t.fillcolor(colour); t.color("white", colour)
    t.begin_fill()
    t.goto(x + size, y + size // 2)
    t.goto(x, y + size)
    t.goto(x, y)
    t.end_fill()
    # Cannon
    t.penup(); t.goto(x + size, y + size // 2)
    t.pendown(); t.goto(x + size + size // 3, y + size // 2)
    # Label
    t.penup(); t.goto(x, y - 15)
    t.color("white"); t.write(name, font=("Arial", 8, "normal"))
    t.color("silver")

draw_ship(-280, -30, 50, "red", "Battle-Hawk")
draw_ship(-80, -30, 50, "cyan", "Nebula-Scout")
draw_ship(120, -30, 50, "gold", "Star-Crusher")

t.penup(); t.goto(-130, 80)
t.color("white"); t.write("🚀 Space Gallery 🚀", font=("Arial", 13, "bold"))

print()
print("🎉 Boss Quest completed!")
print("🏆 You have defeated the Commander!")
print("⭐ Title earned: Hologram Master of Nebula-7")

t.hideturtle(); turtle.done()