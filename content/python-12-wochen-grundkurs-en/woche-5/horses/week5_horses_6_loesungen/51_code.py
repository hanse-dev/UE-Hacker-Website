def can_train(fitness, duration):
    return fitness >= duration * 2

print(f"Stormwind: {can_train(90, 40)}")
print(f"Lightning: {can_train(60, 40)}")
