# Solution suggestion Mission 2 – The Polymorphic Training

# Step 1: Three training classes
class Dressage:
    def __init__(self, name):
        self.name = name

    def training(self):
        print(f"[{self.name}] Practice Piaffe – trot on the spot, elegant and precise!")

class Jumping:
    def __init__(self, name):
        self.name = name

    def training(self):
        print(f"[{self.name}] Jump the course – obstacles in the right order!")

class Western:
    def __init__(self, name):
        self.name = name

    def training(self):
        print(f"[{self.name}] Ride the slalom – relaxed and calm between the poles!")

# Step 2: Polymorphic function
def train_horse(horse_name, training):
    print(f"Horse '{horse_name}' participates in training:")
    training.training()

# Step 3: Test all trainings
dressage_class = Dressage("Dressage")
jumping_course = Jumping("Jumping")
western_course = Western("Western")

train_horse("Valencia", dressage_class)
train_horse("Falcon", jumping_course)
train_horse("Navajo", western_course)

# Bonus: Trainer factory
def trainer_factory(type_, name):
    if type_ == "dressage":
        return Dressage(name)
    elif type_ == "jumping":
        return Jumping(name)
    elif type_ == "western":
        return Western(name)
    else:
        print(f"Unknown training type: {type_}")
        return None

print()
new_training = trainer_factory("jumping", "Advanced Jumping")
train_horse("Champion", new_training)
