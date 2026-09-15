# Example 1: Scan result
signals = 18
if signals >= 15:
    print("⚔️ Life forms detected!")
else:
    print("💨 Sector empty.")

# Example 2: System check
pressure_ok = False
if pressure_ok:
    print("🍺 Pressure chambers operational.")
else:
    print("🚫 Pressure drop detected!")

# Example 3: Energy check
energy = 45
consumption = 50
if energy >= consumption:
    print(f"💰 Jump possible! Remaining: {energy - consumption}%")
else:
    print(f"❌ Jump impossible! Missing: {consumption - energy}%")