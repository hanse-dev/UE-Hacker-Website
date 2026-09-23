q1 = True
q2 = True
q3 = False
q4 = True
q5 = False
points = 0
if q1:
    points = points + 100
if q2:
    points = points + 100
if q3:
    points = points + 100
if q4:
    points = points + 100
if q5:
    points = points + 100
if points >= 400:
    grade = "A"
elif points >= 300:
    grade = "B"
else:
    grade = "C"
print(f"Points: {points}, Grade: {grade}")
