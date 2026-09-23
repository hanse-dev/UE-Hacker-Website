text = "ten"
try:
    number = int(text)
except ValueError:
    number = 0
print(f"Number: {number}")
