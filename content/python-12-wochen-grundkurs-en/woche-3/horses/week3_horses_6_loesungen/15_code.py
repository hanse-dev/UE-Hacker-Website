# Step 1 – Tournament data
points = 90
errors = 0
time = 55  # seconds

# Step 2 – Total score
score = points - (errors * 5) - (time / 10)
print(f"Points: {points}, Errors: {errors}, Time: {time}s")
print(f"Total score: {score:.1f}")

# Step 3 – Gold medal
if score >= 85 and errors == 0:
    print("🥇 GOLD! Perfect ride!")
elif score >= 70 and errors <= 2:
    print("🥈 SILVER! Very good ride!")
elif score >= 50:
    print("🥉 BRONZE! Solid ride.")
else:
    print("No medal this time.")

# Step 5 – Perfect time bonus
if time < 60:
    print("+10 bonus for perfect time!")
