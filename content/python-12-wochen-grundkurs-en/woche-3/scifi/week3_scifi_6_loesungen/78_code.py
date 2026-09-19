phase1_ok = True
phase2_ok = True
phase3_ok = False
phase4_ok = True
phase5_ok = True
successful_phases = 0
if phase1_ok:
    successful_phases += 1
if phase2_ok:
    successful_phases += 1
if phase3_ok:
    successful_phases += 1
if phase4_ok:
    successful_phases += 1
if phase5_ok:
    successful_phases += 1
print(f"Successful phases: {successful_phases}")
