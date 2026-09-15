# ✨ Examples of good and bad names

# ✅ Good names (clear and descriptive)
def calculate_feed_amount(weight, activity):
    """Calculates the daily feed amount."""
    return weight * activity * 0.02

def find_best_training(horses_list):
    """Finds the best training for a list of horses."""
    return max(horses_list)

def is_horse_available(horse_id, time_slot):
    """Checks whether a horse is available."""
    return horse_id not in booked_horses[time_slot]

# ❌ Bad names (unclear or wrong convention)
# def CalculateFeedAmount():  # CamelCase
# def fa(w, a):  # Too short, not descriptive
# def feeding_calculation():  # Noun first

print("=== Good Function Names in Action ===")
feed = calculate_feed_amount(500, 1.5)
print(f"Feed amount: {feed} kg")

trainings = ["Dressage", "Jumping", "Western"]
best_training = find_best_training(trainings)
print(f"Best training: {best_training}")

# Example data for availability check
booked_horses = {"morning": ["Bobby", "Luna"], "midday": []}
available = is_horse_available("Storm", "morning")
print(f"Horse available: {available}")