# Example 2: For loop with start and end
print("=== Example 2: Scanning Sectors 3 to 7 ===")
# range(3, 8) generates the numbers 3, 4, 5, 6, 7 (8 is exclusive!)
for sector in range(3, 8):
    print(f"Sector {sector}: Scan complete")

print("\n=== Important observation ===")
print("range(start, end) includes start, but not end!")
print("Like coordinates: from 3 up to BEFORE 8")