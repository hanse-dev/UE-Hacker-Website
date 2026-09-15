# 🔍 Exercises with return

# Example 1: Simple calculation with return
def calculate_warp_distance(warp_factor, time):
    """Calculates the distance traveled in warp"""
    distance = warp_factor * time * 1000
    return distance

# Store result in a variable
print("=== Warp Distance Calculation ===")
distance1 = calculate_warp_distance(5, 10)
print(f"Jump 1: {distance1} light-years")

distance2 = calculate_warp_distance(8, 15)
print(f"Jump 2: {distance2} light-years")

# Use result directly
print(f"Emergency jump: {calculate_warp_distance(10, 5)} light-years")