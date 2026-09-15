# Step 1 – Quiz answers (True = correct, False = wrong)
answer1 = True   # Question 1: Correct
answer2 = True   # Question 2: Correct
answer3 = True   # Question 3: Correct
answer4 = False  # Question 4: Wrong
answer5 = True   # Question 5: Correct

# Steps 2 & 3 – Check answers and count points
points = 0

print("=== RIDER QUIZ EVALUATION ===")
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
    print("🎖️ === RIDER CERTIFICATE ===")
    print("This certifies that this rider")
    print("has successfully passed the Rider Quiz!")
    print(f"Score: {points} | Grade: {grade}")
    print("Signature: Stable Master William")
else:
    print("Unfortunately not passed. Keep practicing!")
