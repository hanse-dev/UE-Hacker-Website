import turtle

t = turtle.Turtle()
screen = turtle.Screen()
screen.bgcolor("lightyellow")
t.speed(10)

def zeichne_pferd(x, y, groesse, farbe):
    t.penup(); t.goto(x, y)
    t.fillcolor(farbe); t.color("brown", farbe)
    # Körper (Oval vereinfacht als Rechteck)
    t.pendown(); t.begin_fill()
    for _ in range(2):
        t.forward(groesse * 2); t.left(90)
        t.forward(groesse); t.left(90)
    t.end_fill()
    # Kopf
    t.penup(); t.goto(x + groesse * 2, y + groesse * 0.7)
    t.begin_fill(); t.circle(groesse * 0.4); t.end_fill()
    # Beine
    t.pendown()
    for bein_x in [x + 0.3*groesse, x + 0.6*groesse, x + 1.2*groesse, x + 1.6*groesse]:
        t.penup(); t.goto(bein_x, y)
        t.pendown(); t.goto(bein_x, y - groesse * 0.8)
    # Name
    t.penup(); t.goto(x + groesse, y - groesse - 10)
    t.color("black"); t.write(farbe.title(), align="center", font=("Arial", 8, "normal"))

zeichne_pferd(-280, -20, 40, "brown")
zeichne_pferd(-80, -20, 40, "gray")
zeichne_pferd(120, -20, 40, "black")

t.penup(); t.goto(0, 90)
t.write("🐴 Pferde-Galerie 🐴", align="center", font=("Arial", 14, "bold"))
t.hideturtle(); turtle.done()