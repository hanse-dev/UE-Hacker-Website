# Step 1 – Quiz answers (True = correct, False = wrong)
answer1 = True   # Question 1: Correct
answer2 = True   # Question 2: Correct
answer3 = False  # Question 3: Wrong
answer4 = True   # Question 4: Correct
answer5 = True   # Question 5: Correct

# Steps 2 & 3 – Check and count points
points = 0

print("=== MAGIC QUIZ EVALUATION ===")
if answer1:
    print("Question 1: ✅ Correct! +100 points")
    points += 100
else:
    print("Question 1: ❌ Wrong!")

if answer2:
    print("Question 2: ✅ Correct! +100 points")
    points += 100
else:
    print("Question 2: ❌ Wrong!")

if answer3:
    print("Question 3: ✅ Correct! +100 points")
    points += 100
else:
    print("Question 3: ❌ Wrong!")

if answer4:
    print("Question 4: ✅ Correct! +100 points")
    points += 100
else:
    print("Question 4: ❌ Wrong!")

if answer5:
    print("Question 5: ✅ Correct! +100 points")
    points += 100
else:
    print("Question 5: ❌ Wrong!")

print()
print(f"Total points: {points} / 500")

# Step 4 – Final rating
if points >= 400:
    grade = "A"
elif points >= 300:
    grade = "B"
elif points >= 200:
    grade = "C"
else:
    grade = "D"
print(f"Grade: {grade}")

# Step 5 – Certificate
if points >= 300:
    print()
    print("🎖️ === MAGIC CERTIFICATE ===")
    print("This certifies that this hero")
    print("has passed the Magic Quiz!")
    print(f"Score: {points} | Grade: {grade}")
    print("Signed: Grand Spell Master")
else:
    print("Not passed. Try again!")