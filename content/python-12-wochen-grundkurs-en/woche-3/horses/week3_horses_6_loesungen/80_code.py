obstacle_knocked = True
horse_spooked = False
saddle_slipped = True
penalty = 0
if obstacle_knocked:
    penalty = penalty + 10
if horse_spooked:
    penalty = penalty + 15
if saddle_slipped:
    penalty = penalty + 5
print(f"Penalty: {penalty}")