import random

# Step 1 – Variables
energy = 100
distance = 0
breaks = 0
special_events = []

print("=== MARATHON RIDE STARTS ===")
print(f"Starting energy: {energy}")
print()

# Step 1 – Main marathon loop
while True:
    distance += 1

    # Step 2 – Energy usage
    usage = random.randint(5, 15)
    energy -= usage

    # Step 3 – Feed break every 8 rounds
    if distance % 8 == 0:
        feed_bonus = random.randint(10, 25)
        energy += feed_bonus
        if energy > 100:
            energy = 100
        breaks += 1
        event = f"Round {distance}: Feed break! +{feed_bonus} energy"
        special_events.append(event)
        print(event)

    # Step 3 – Energy used up
    if energy <= 0:
        print(f"😴 Horse exhausted after {distance} rounds!")
        break

    # Status message every 10 rounds
    if distance % 10 == 0:
        print(f"Round {distance}: Energy={energy}")

    if distance >= 100:
        print(f"🏆 Marathon Champion! 100 rounds completed!")
        break

# Step 4 – Statistics
print()
print("=== MARATHON RESULTS ===")
print(f"Total distance: {distance} rounds")
print(f"Feed breaks: {breaks}")
print(f"Final energy: {energy}")
print(f"Special events: {len(special_events)}")

print()
print("🎉 Final Challenge completed!")
print("🏆 You have mastered the horse of endless rounds!")
print("⭐ Title earned: Master of Rhythm")
print()
print("🎊 CONGRATULATIONS! You have mastered Week 4!")
print("🐴 Next week: Functions (def, return)!")