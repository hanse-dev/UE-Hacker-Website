# Step 1: 3D coordinates as tuples
pos1 = (100, 200, 50)
pos2 = (300, -150, 80)
print(f"Position 1: {pos1}, Length: {len(pos1)}")
print(f"Position 2: {pos2}, Length: {len(pos2)}")

# Step 2: Tuple unpacking
x1, y1, z1 = pos1
print(f"X={x1}, Y={y1}, Z={z1}")

# Step 3: Combine with dictionary
coordinates = {
    "start": pos1,
    "target": pos2,
    "distance": ((x1 - pos2[0])**2 + (y1 - pos2[1])**2 + (z1 - pos2[2])**2) ** 0.5
}
print(f"\nRoute: {coordinates['start']} → {coordinates['target']}")
print(f"Distance: {coordinates['distance']:.1f} light years")