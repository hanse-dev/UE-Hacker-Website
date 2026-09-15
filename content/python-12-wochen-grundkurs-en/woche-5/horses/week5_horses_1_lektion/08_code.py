# Example 3: Function with multiple parameters
def create_horse_profile(name, breed, age):
    """Creates a horse profile with name, breed and age"""
    print(f"Horse Profile:")
    print(f"  Name: {name}")
    print(f"  Breed: {breed}")
    print(f"  Age: {age} years")
    print(f"  Status: Ready for training!")

# Create various horse profiles
print("=== Horse Profiles ===")
create_horse_profile("Bobby", "Hanoverian", 8)
print()
create_horse_profile("Luna", "Icelandic", 5)
print()
create_horse_profile("Storm", "Quarter Horse", 6)