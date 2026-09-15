import random

# Step 1 – Starting conditions
health = 100
mana = 80
depth = 0
total_treasure = 0
special_events = []

print("=== THE ENDLESS DUNGEON ===")
print(f"Start: Health={health}, Mana={mana}")
print()

# Step 1 – Infinite loop
while True:
    depth += 1

    # Step 2 – Random treasure value
    treasure = random.randint(5, 50)
    total_treasure += treasure

    # Step 2 – Consume health and mana
    damage = random.randint(5, 20)
    mana_loss = random.randint(3, 10)
    health -= damage
    mana -= mana_loss

    # Step 4 – Healing sources every 5 rooms
    if depth % 5 == 0:
        healing = random.randint(15, 30)
        health += healing
        if health > 100:
            health = 100
        event = f"Room {depth}: Healing spring! +{healing} health"
        special_events.append(event)
        print(event)

    # Step 3 – Check death
    if health <= 0:
        print(f"💀 Hero dies in room {depth}! Treasure: {total_treasure} gold")
        break

    if mana <= 0:
        print(f"🔮 Mana exhausted in room {depth}! Treasure: {total_treasure} gold")
        break

    # Status display every 10 rooms
    if depth % 10 == 0:
        print(f"Depth {depth}: Health={health}, Mana={mana}, Treasure={total_treasure}")

    if depth >= 100:
        print(f"🏆 Dungeon Legend! {depth} rooms survived!")
        break

print()
print("=== DUNGEON SUMMARY ===")
print(f"Depth reached: {depth} rooms")
print(f"Total treasure: {total_treasure} gold")
print(f"Special events: {len(special_events)}")

print()
print("🎉 Boss Quest completed!")
print("🏆 You have defeated the endless cyclop!")
print("⭐ Title earned: Master of Cycles")
print()
print("🎊 CONGRATULATIONS! You have mastered Week 4!")
print("📚 Next week: Functions (def, return)!")