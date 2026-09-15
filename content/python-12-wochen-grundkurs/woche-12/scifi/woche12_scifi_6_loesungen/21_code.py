import turtle

t = turtle.Turtle(); t.speed(10)
screen = turtle.Screen()
screen.bgcolor("black")

def zeichne_schiff(x, y, groesse, farbe, name):
    t.penup(); t.goto(x, y); t.pendown()
    t.fillcolor(farbe); t.begin_fill()
    t.goto(x + groesse, y + groesse // 2)
    t.goto(x, y + groesse)
    t.goto(x, y)
    t.end_fill()
    # Kanone
    t.penup(); t.goto(x + groesse, y + groesse // 2)
    t.pendown(); t.goto(x + groesse + groesse // 3, y + groesse // 2)
    # Name
    t.penup(); t.goto(x, y - 15)
    t.color("white"); t.write(name, font=("Arial", 8, "normal"))
    t.color("silver")

zeichne_schiff(-280, -30, 50, "red", "Battle-Hawk")
zeichne_schiff(-80, -30, 50, "cyan", "Nebula-Scout")
zeichne_schiff(120, -30, 50, "gold", "Star-Crusher")

t.penup(); t.goto(-130, 80)
t.color("white"); t.write("🚀 Raumschiff-Galerie 🚀", font=("Arial", 13, "bold"))

print()
print("🎉 Boss-Quest abgeschlossen!")
print("🏆 Du hast den Kommandanten besiegt!")
print("⭐ Titel erhalten: Hologramm-Meister der Nebula-7")

t.hideturtle(); turtle.done()