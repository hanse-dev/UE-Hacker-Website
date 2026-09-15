successes = 0
print("=== SPACESHIP SIMULATOR STARTED ===")
print()

# Level 1: Launch sequence
energy = 80
system_ok = True
if energy >= 50 and system_ok:
    print("Level 1 ✅ – Launch sequence successful! All systems online.")
    successes += 1
else:
    print("Level 1 ❌ – Launch sequence failed!")

# Level 2: Course selection
course = "North"
if course == "North":
    print("Level 2 ✅ – Course North set. Heading to Andromeda!")
    successes += 1
else:
    print("Level 2 ✅ – Course South set. Heading to Centaurus!")
    successes += 1

# Level 3: Speed
speed = 650
if speed >= 900:
    print("Level 3 ✅ – WARP! Speed of light reached!")
    successes += 1
elif speed >= 700:
    print("Level 3 ✅ – Very fast! Sub-warp drive active.")
    successes += 1
elif speed >= 500:
    print("Level 3 ✅ – Good cruising speed.")
    successes += 1
elif speed >= 200:
    print("Level 3 ❌ – Too slow for this mission!")
else:
    print("Level 3 ❌ – Drive nearly without thrust!")

# Level 4: Systems check
shields = 85
weapons = 70
drive = 90
if shields >= 70:
    if weapons >= 60:
        print("Level 4 ✅ – Shields and weapons ready for action!")
        successes += 1
    else:
        print("Level 4 ❌ – Weapon systems too weak!")
else:
    print("Level 4 ❌ – Shields too low – danger!")

# Level 5: Emergency landing
fuel = 25
atmosphere = True
landing_spot = True
if fuel >= 20 or (atmosphere and landing_spot):
    print("Level 5 ✅ – Emergency landing successful! Landed safely.")
    successes += 1
else:
    print("Level 5 ❌ – Emergency landing failed!")

# Result
print()
print(f"=== RESULT: {successes}/5 levels passed ===")
if successes == 5:
    print("🏆 PILOT LICENSE EARNED! Perfect simulator run!")
elif successes >= 3:
    print("⭐ Good! A little more practice needed.")
else:
    print("💪 Keep simulating – you will get better!")