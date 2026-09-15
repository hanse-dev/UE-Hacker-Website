# Example 4: For loop over a string
print("=== Example 4: Letters of a Code ===")
code = "ALPHA"
print(f"The code is: {code}")
print("Letter by letter:")

for letter in code:
    print(f"  - {letter}")

print("\n=== What happens here? ===")
print("String is treated as a sequence of letters")
print("Each letter is iterated individually")