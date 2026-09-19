# Mission 2: The healing item
world["lab"]["items"].append(Item("Medkit", "Restores 10 hit points."))

def use(self, item_name):
    for item in self.inventory:
        if item.name == item_name:
            if item_name == "Medkit":
                self.hp += 10
                self.inventory.remove(item)
                print(f"🧪 You use the {item_name}. You now have {self.hp} HP.")
            else:
                print(f"🤷 You can't do anything with the {item_name} here.")
            return
    print(f"❓ You don't have a '{item_name}' in your bag.")

Player.use = use

hero = Player("Ben", "lab")
hero.hp = 5
hero.take("Medkit")
hero.use("Medkit")
hero.use("Medkit")