import random
import math

# Step 1: Horse selection
horse_names = ["Thunder", "Luna", "Blitz", "Silver", "Storm", "Cloud"]
chosen_horse = random.choice(horse_names)
print("=== Sunny Valley Ranch ===")
print(f"All horses: {horse_names}")
print(f"Today's horse of the day: {chosen_horse}")

# Step 2: Weather simulation
print("\nWeather forecast (3 days):")
days = ["Monday", "Tuesday", "Wednesday"]
for day in days:
    temperature = round(random.uniform(-10, 30), 1)
    print(f"  {day}: {temperature}°C")

# Step 3: Feed consumption
print("\nFeed plan:")
feed_horses = ["Thunder", "Luna", "Blitz"]
total_feed = 0
for horse in feed_horses:
    feed = random.randint(5, 15)
    total_feed += feed
    print(f"  {horse}: {feed} kg")
print(f"  Total: {total_feed} kg")

# Step 4: Horse generator with speed
print("\nSpeed ranking:")
race_horses = [(name, random.randint(1, 10)) for name in ["Blitz", "Storm", "Silver"]]
for name, speed in race_horses:
    print(f"  {name}: Speed {speed}/10")

# Bonus: Normal distribution
feed_gauss = round(random.gauss(10, 2), 1)
print(f"\nBonus – Gauss feed amount: {feed_gauss} kg")