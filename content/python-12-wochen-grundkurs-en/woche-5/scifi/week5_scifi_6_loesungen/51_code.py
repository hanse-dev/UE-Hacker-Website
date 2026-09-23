def is_serviceable(energy, duration):
    return energy >= duration * 2

print(f"Nebula: {is_serviceable(90, 40)}")
print(f"Comet: {is_serviceable(60, 40)}")
