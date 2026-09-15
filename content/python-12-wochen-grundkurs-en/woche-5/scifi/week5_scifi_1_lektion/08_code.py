# Example 3: Function with multiple parameters
def create_ship_profile(name, ship_class, crew):
    """Creates a ship profile with name, class, and crew"""
    print(f"Ship Profile:")
    print(f"  Name: {name}")
    print(f"  Class: {ship_class}")
    print(f"  Crew: {crew} members")
    print(f"  Status: Ready for deployment!")

# Create different ship profiles
print("=== Ship Profiles ===")
create_ship_profile("Nebula-Explorer", "Research Vessel", 150)
print()
create_ship_profile("Star-Fighter", "Fighter", 2)
print()
create_ship_profile("Cargo-Hauler", "Freighter", 25)