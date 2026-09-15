# Example 3: Access codes
print("=== Example 3: Access Codes ===")
code = ""
attempts = 0
max_attempts = 3

while code != "NEXUS" and attempts < max_attempts:
    code = input("Enter the access code: ")
    attempts += 1
    
    if code == "NEXUS":
        print("✅ Access granted!")
    elif attempts >= max_attempts:
        print("❌ Too many attempts! System locked.")
    else:
        print(f"Wrong! {max_attempts - attempts} attempts remaining")