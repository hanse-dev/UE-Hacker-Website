import random

def create_mission_profile(name, target, priority):
    """Creates a mission profile.
    
    Parameters:
        name (str): Name of the mission
        target (str): Target coordinates or description
        priority (int): Priority level (1 = low, 5 = highest)
    
    Returns:
        dict: Dictionary with name, target, priority
    """
    return {"name": name, "target": target, "priority": priority}

def calculate_travel_time(distance, speed):
    return distance / speed

def generate_report(profile, travel_time):
    report = "=== MISSION REPORT ===\n"
    report += f"Name:      {profile['name']}\n"
    report += f"Target:    {profile['target']}\n"
    report += f"Priority:  {profile['priority']}/5\n"
    report += f"Travel:    {travel_time:.1f} hours\n"
    report += "=" * 22
    return report

profile = create_mission_profile("Omega-Scan", "Sector Delta-9", 4)
travel_time = calculate_travel_time(450, 30)
print(generate_report(profile, travel_time))

def random_space_weather():
    weather = random.choice(["calm", "Meteor Storm", "Solar Wind"])
    obstacle = random.choice(["none", "Asteroid Field", "Space Pirates"])
    return weather, obstacle

weather, obstacle = random_space_weather()
print(f"Space weather: {weather} | Obstacle: {obstacle}")