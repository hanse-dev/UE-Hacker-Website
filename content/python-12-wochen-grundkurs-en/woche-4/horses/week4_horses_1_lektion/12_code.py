# Example 3: Feed quiz
print("=== Example 3: Feed quiz ===")
feed = ""
attempts = 0
max_attempts = 3

while feed != "Hay" and attempts < max_attempts:
    feed = input("What do horses love to eat most? ")
    attempts += 1
    
    if feed == "Hay":
        print("✅ Correct!")
    elif attempts >= max_attempts:
        print("❌ Too many attempts! The answer is: Hay")
    else:
        print(f"Wrong! {max_attempts - attempts} attempts remaining")