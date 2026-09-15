# Example 3: Validate user input
print("=== Example 3: Password check ===")
password = ""
attempts = 0
max_attempts = 3

while password != "Secret" and attempts < max_attempts:
    password = input("Enter the password: ")
    attempts += 1
    
    if password == "Secret":
        print("✅ Access granted!")
    elif attempts >= max_attempts:
        print("❌ Too many attempts!")
    else:
        print(f"Wrong! {max_attempts - attempts} attempts remaining")