# Step 1: Create disciplines
tournament_plan = {
    "Dressage": {"judge": "Dr. Weber", "time": "09:00", "max_participants": 8, "participants": []},
    "Jumping": {"judge": "Ms. Schmidt", "time": "11:00", "max_participants": 6, "participants": []},
    "Cross-Country": {"judge": "Mr. Miller", "time": "14:00", "max_participants": 10, "participants": []}
}

# Step 2: Assign a rider
rider = {"name": "Lena", "level": 3, "horse": "Thunder"}
tournament_plan["Dressage"]["participants"].append(rider["name"])
tournament_plan["Jumping"]["participants"].append(rider["name"])

# Step 3: Print overview
print("=== TOURNAMENT SCHEDULE ===")
for discipline, info in tournament_plan.items():
    free_spots = info["max_participants"] - len(info["participants"])
    status = "Spots available" if free_spots > 0 else "Fully booked!"
    print(f"\n{discipline}:")
    print(f"  Judge:           {info['judge']}")
    print(f"  Time:            {info['time']}")
    print(f"  Participants:    {info['participants']}")
    print(f"  Free spots:      {free_spots} – {status}")

# Bonus: Times as tuple
times = tuple(info["time"] for info in tournament_plan.values())
print(f"\nBonus – Schedule: {times}")