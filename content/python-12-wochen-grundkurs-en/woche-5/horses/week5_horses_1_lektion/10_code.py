# 🔍 Exercises with return

# Example 1: Simple calculation with return
def calculate_training_time(sessions, duration_per_session):
    """Calculates the total training time"""
    total_time = sessions * duration_per_session
    return total_time

# Store result in variable
print("=== Training Time Calculation ===")
time1 = calculate_training_time(5, 15)
print(f"Training 1: {time1} minutes")

time2 = calculate_training_time(3, 20)
print(f"Training 2: {time2} minutes")

# Use result directly
print(f"Intensive training: {calculate_training_time(10, 30)} minutes")