def calculate_duration(laps):
    return laps * 5

def can_train(fitness, duration):
    return fitness >= duration * 2
def show_training(name, fitness, laps):
    duration = calculate_duration(laps)
    if can_train(fitness, duration):
        print(f"{name}: training {duration} minutes")
    else:
        print(f"{name}: needs a break")

show_training("Stormwind", 90, 8)
show_training("Lightning", 60, 8)
