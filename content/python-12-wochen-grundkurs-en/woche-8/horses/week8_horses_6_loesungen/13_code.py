import math

# Step 1: Coordinates as tuples
pos1 = (0, 0)      # Stable
pos2 = (50, 30)    # Arena
print(f"Start (Stable):    {pos1} | Length: {len(pos1)}")
print(f"End (Arena):       {pos2} | Length: {len(pos2)}")

# Step 2: Tuple unpacking
x1, y1 = pos1
print(f"\nStable: x={x1}, y={y1}")
x2, y2 = pos2
print(f"Arena: x={x2}, y={y2}")

# Step 3: Positions dictionary
positions = {
    "Stable": (0, 0),
    "Arena": (50, 30),
    "Pasture": (100, 80),
    "Tournament Track": (200, 150)
}
print(f"\nPositions dictionary: {positions}")
print(f"Arena position: {positions['Arena']}")

# Step 4: Distance calculation
def distance(coord1, coord2):
    x1, y1 = coord1
    x2, y2 = coord2
    return round(math.sqrt((x2 - x1)**2 + (y2 - y1)**2), 2)

a = distance(positions["Stable"], positions["Arena"])
print(f"\nDistance Stable → Arena: {a} m")
b = distance(positions["Arena"], positions["Pasture"])
print(f"Distance Arena → Pasture: {b} m")

# Bonus: 3D coordinates
pos_3d_1 = (0, 0, 0)
pos_3d_2 = (50, 30, 10)
x1, y1, z1 = pos_3d_1
x2, y2, z2 = pos_3d_2
distance_3d = round(math.sqrt((x2-x1)**2 + (y2-y1)**2 + (z2-z1)**2), 2)
print(f"\nBonus 3D distance: {distance_3d} m")