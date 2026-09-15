successes = 0
print("=== DUNGEON SIMULATOR STARTED ===")
print()

# Level 1: Summoning
mana = 75
spell_ready = True
if mana >= 50 and spell_ready:
    print("Level 1 ✅ – Summoning succeeds! Mana sufficient and spell ready.")
    successes += 1
else:
    print("Level 1 ❌ – Summoning failed!")

# Level 2: Path choice
path = "Left"
if path == "Left":
    print("Level 2 ✅ – You go Left. The treasure lies there!")
    successes += 1
else:
    print("Level 2 ❌ – Right was the trap. Go back!")

# Level 3: Speed
speed = 65
if speed >= 90:
    print("Level 3 ✅ – LIGHTNING speed! Unstoppable!")
    successes += 1
elif speed >= 70:
    print("Level 3 ✅ – Fast! You escape the monster!")
    successes += 1
elif speed >= 50:
    print("Level 3 ✅ – Good speed, you make it through.")
    successes += 1
elif speed >= 30:
    print("Level 3 ❌ – Too slow, the monster catches you!")
else:
    print("Level 3 ❌ – Way too slow!")

# Level 4: Magic trial
shield = 80
attack = 70
healing = 60
if shield >= 70:
    if attack >= 60:
        print("Level 4 ✅ – Shield and attack strong enough!")
        successes += 1
    else:
        print("Level 4 ❌ – Attack too weak!")
else:
    print("Level 4 ❌ – Shield too low!")

# Level 5: Escape
potions = 4
runes = True
escape_route = True
if potions >= 3 or (runes and escape_route):
    print("Level 5 ✅ – Escape succeeds! Got away!")
    successes += 1
else:
    print("Level 5 ❌ – No escape!")

# Result
print()
print(f"=== RESULT: {successes}/5 Levels passed ===")
if successes == 5:
    print("🏆 DUNGEON MASTER! Perfect run!")
elif successes >= 3:
    print("⭐ Well done! But there is still room for improvement.")
else:
    print("💪 Keep practicing – you can do it!")