count = 0
for i in range(5):
    height = 90 + i * 10
    
    if height > 100:
        count += 1
print(f"Higher than 100 cm: {count}")
