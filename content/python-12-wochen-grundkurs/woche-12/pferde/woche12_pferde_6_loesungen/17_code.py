import turtle

t = turtle.Turtle()
screen = turtle.Screen()
screen.bgcolor("green")
screen.title("Reiterhof Sonnental")
t.speed(8)

def rechteck(x, y, breite, hoehe, farbe, beschriftung):
    t.penup(); t.goto(x, y); t.pendown()
    t.fillcolor(farbe); t.begin_fill()
    for _ in range(2):
        t.forward(breite); t.left(90)
        t.forward(hoehe); t.left(90)
    t.end_fill()
    t.penup(); t.goto(x + breite/2, y + hoehe/2 - 8)
    t.write(beschriftung, align="center", font=("Arial", 9, "bold"))

rechteck(-250, 50, 120, 80, "brown", "Stall")
rechteck(-100, 30, 150, 100, "lightblue", "Reitbahn")
rechteck(80, 50, 120, 80, "lightgreen", "Weide")
rechteck(-250, -120, 100, 60, "beige", "Wohnhaus")

t.hideturtle(); turtle.done()