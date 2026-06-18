# 🐢 Turtle Graphics Cheat Sheet

Welcome to the ultimate Turtle command overview! Here you'll find all the important commands for your graphical projects.

## 📋 Basics

### Import and setup
```python
import turtle  # Import the Turtle module

# Set up the screen
screen = turtle.Screen()
screen.title("My Turtle Project")
screen.bgcolor("black")
screen.setup(800, 600)  # Width, height

# Create a turtle
pen = turtle.Turtle()
pen.speed(5)  # 1=slow, 10=fast, 0=instant
```

### End the program
```python
turtle.done()  # Important at the end!
```

## 🎨 Movement commands

### Forward and backward
```python
pen.forward(100)      # 100 pixels forward
pen.backward(50)      # 50 pixels backward
pen.fd(100)          # Short form for forward
pen.bk(50)           # Short form for backward
```

### Turning
```python
pen.left(90)         # Turn 90 degrees left
pen.right(45)        # Turn 45 degrees right
pen.lt(90)           # Short form for left
pen.rt(45)           # Short form for right

# Turn to an absolute angle
pen.setheading(0)    # Face east
pen.setheading(90)   # Face north
pen.setheading(180)  # Face west
pen.setheading(270)  # Face south
```

### Positioning
```python
pen.goto(100, 50)    # Move to coordinate (x, y)
pen.setx(100)        # Change only the X position
pen.sety(50)         # Change only the Y position
pen.home()           # Return to start point (0, 0)
```

## ✏️ Pen control

### Pen up/down
```python
pen.penup()          # Lift pen (don't draw)
pen.pendown()        # Lower pen (draw)
pen.up()             # Short form for penup
pen.down()           # Short form for pendown
```

### Pen status
```python
pen.isdown()         # True if pen is down
pen.isup()           # True if pen is up
```

## 🎨 Colours and fills

### Setting colours
```python
pen.color("red")                     # Pen colour
pen.color("red", "blue")             # Pen colour, fill colour
pen.pencolor("green")                # Pen colour only
pen.fillcolor("yellow")              # Fill colour only

# RGB colours (0-255)
pen.pencolor(255, 0, 0)              # Red
pen.fillcolor(0, 255, 0)             # Green
```

### Fills
```python
pen.begin_fill()                     # Start fill
# Draw your shape here
pen.end_fill()                       # End fill

# Fill status
pen.filling()                        # True if currently filling
```

### Background colour
```python
screen.bgcolor("lightblue")          # Change background colour
```

## 📏 Line properties

### Line width
```python
pen.pensize(5)                       # Line width 5 pixels
pen.width(3)                         # Alternative for pensize
```

### Line style
```python
pen.resizemode("user")               # Allow resizing
pen.turtlesize(2, 2)                 # Turtle size (width, height)
```

## 🔷 Drawing shapes

### Circle
```python
pen.circle(50)                       # Circle with radius 50
pen.circle(50, 180)                  # Semicircle (180 degrees)
pen.circle(50, steps=5)              # Pentagon
```

### Dot
```python
pen.dot(20, "red")                   # Dot with size 20 and colour
pen.dot()                            # Small default dot
```

### Polygon
```python
# Square
for _ in range(4):
    pen.forward(100)
    pen.left(90)

# Triangle
for _ in range(3):
    pen.forward(100)
    pen.left(120)

# Hexagon
for _ in range(6):
    pen.forward(100)
    pen.left(60)
```

## 🐢 Turtle appearance

### Change shape
```python
pen.shape("turtle")                  # Turtle
pen.shape("arrow")                   # Arrow
pen.shape("circle")                  # Circle
pen.shape("square")                  # Square
pen.shape("triangle")                # Triangle
pen.shape("classic")                 # Classic arrow
```

### Visibility
```python
pen.hideturtle()                     # Hide turtle
pen.showturtle()                     # Show turtle
pen.isvisible()                      # True if visible
```

## 📝 Writing text

### Output text
```python
pen.write("Hello World!", font=("Arial", 16, "normal"))
pen.write("Python", font=("Times", 20, "bold"))
pen.write("Turtle", font=("Courier", 14, "italic"))
```

### Text alignment
```python
pen.write("Text", align="center")    # Centred
pen.write("Text", align="right")     # Right-aligned
pen.write("Text", align="left")      # Left-aligned (default)
```

## 🔄 Saving state

### Save current state
```python
position = pen.position()            # Current position
heading = pen.heading()              # Current heading
```

### Restore state
```python
pen.setposition(position)            # Restore position
pen.setheading(heading)              # Restore heading
```

## 🧹 Screen control

### Clear screen
```python
pen.clear()                          # Clear drawings only
screen.clear()                       # Clear everything
pen.reset()                          # Reset turtle
```

### Screen updates
```python
screen.tracer(0)                     # Animation off
screen.update()                      # Update manually
screen.tracer(1)                     # Animation on (default)
```

## 🎯 Useful functions

### Calculate angle
```python
import math
angle = math.degrees(math.atan2(y2-y1, x2-x1))  # Angle between two points
```

### Calculate distance
```python
import math
distance = math.sqrt((x2-x1)**2 + (y2-y1)**2)    # Distance between two points
```

### Random colours
```python
import random
random_colour = random.choice(["red", "blue", "green", "yellow"])
```

## 🎮 Animation tips

### Speed settings
```python
pen.speed(1)                         # Very slow
pen.speed(3)                         # Slow
pen.speed(5)                         # Normal
pen.speed(10)                        # Fast
```

### Delays
```python
import time
time.sleep(1)                        # Wait 1 second
```

### Smooth movement
```python
for i in range(100):
    pen.forward(1)
    pen.left(3.6)                    # Slow rotation
```

## 🐛 Troubleshooting

### Common problems
```python
# Problem: Nothing is drawn
# Solution: forgot pen.pendown() or turtle.done()

# Problem: Turtle is invisible
# Solution: pen.color("white") on a black background

# Problem: Program closes immediately
# Solution: add turtle.done() at the end
```

### Debug info
```python
print(pen.position())               # Print current position
print(pen.heading())                # Current heading
print(pen.isdown())                 # Check pen status
```

## 💡 Pro tips

### Multiple turtles
```python
t1 = turtle.Turtle()
t2 = turtle.Turtle()
t1.color("red")
t2.color("blue")
```

### Functions for shapes
```python
def draw_square(size):
    for _ in range(4):
        pen.forward(size)
        pen.left(90)

# Call it
draw_square(100)
```

### Coordinate system
```python
# Draw axes
pen.color("gray")
pen.goto(-300, 0)
pen.goto(300, 0)
pen.goto(0, -200)
pen.goto(0, 200)
```

## 🎨 Colour palette

### Standard colours
- `"black"`, `"white"`, `"gray"`, `"red"`, `"green"`, `"blue"`
- `"yellow"`, `"orange"`, `"purple"`, `"pink"`, `"brown"`, `"cyan"`

### Special colours
- `"gold"`, `"silver"`, `"maroon"`, `"navy"`, `"olive"`, `"teal"`

### RGB colours
```python
# Pastel colours
pen.pencolor(255, 182, 193)  # Light pink
pen.pencolor(176, 224, 230)  # Light blue
pen.pencolor(152, 251, 152)  # Light green

# Neon colours
pen.pencolor(255, 0, 255)    # Magenta
pen.pencolor(0, 255, 255)    # Cyan
pen.pencolor(255, 255, 0)    # Yellow
```

---

## 🚀 Quick reference

| Category | Command | Example |
|----------|---------|---------|
| **Movement** | forward/backward | `pen.forward(100)` |
| | left/right | `pen.left(90)` |
| | goto | `pen.goto(50, 100)` |
| **Pen** | penup/pendown | `pen.penup()` |
| | color | `pen.color("red")` |
| | pensize | `pen.pensize(3)` |
| **Shapes** | circle | `pen.circle(50)` |
| | dot | `pen.dot(20)` |
| | begin_fill/end_fill | `pen.begin_fill()` |
| **Text** | write | `pen.write("Hello")` |
| **State** | position | `pen.position()` |
| | heading | `pen.heading()` |
| | clear/reset | `pen.clear()` |

---

**Have fun drawing! 🎨**
