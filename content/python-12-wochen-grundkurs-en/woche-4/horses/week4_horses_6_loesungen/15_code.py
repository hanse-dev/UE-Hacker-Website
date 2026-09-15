import random

# Step 1 – Variables
stamina = 100
rounds = 0
max_stamina = stamina

print("=== ENDURANCE TRAINING STARTS ===")
print(f"Starting stamina: {stamina}")
print()

# Step 1 – Main training loop
while True:
    rounds += 1

    # Step 2 – Use up stamina
    usage = random.randint(3, 8)
    stamina -= usage

    # Step 4 – Status message every 5 rounds
    if rounds % 5 == 0:
        print(f"Round {rounds}: Stamina = {stamina}")

    # Step 3 – Stop immediately when stamina < 10
    if stamina < 10:
        print(f"⚠️ Stamina critical in round {rounds}! Training stopped.")
        break

    # Step 3 – Champion after 50 rounds
    if rounds >= 50:
        print(f"🏆 Champion! 50 rounds completed!")
        break

# Summary
print()
print("=== TRAINING REPORT ===")
print(f"Total rounds: {rounds}")
print(f"Final stamina: {stamina}")
if rounds >= 50:
    print("Rating: CHAMPION RIDER 🏆")
elif rounds >= 30:
    print("Rating: Very good stamina ⭐")
else:
    print("Rating: Keep training 💪")