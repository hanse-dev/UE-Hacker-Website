# Example 4: For loop over a string
print("=== Example 4: Letters of a name ===")
name = "Aria"
print(f"The name is: {name}")
print("Letter by letter:")

for letter in name:
    print(f"  - {letter}")

print("\n=== What happens here? ===")
print("The string is treated as a sequence of letters")
print("Each letter is visited one at a time")