successful_phases = 4
danger_level = 4
total_points = successful_phases * 100 - danger_level * 20
success_rate = (successful_phases / 5) * 100
print(f"Total points: {total_points}, Success rate: {success_rate}%")
