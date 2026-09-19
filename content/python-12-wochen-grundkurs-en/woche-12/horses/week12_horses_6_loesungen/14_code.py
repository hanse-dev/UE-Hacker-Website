# Mission 2: The healing item
world["tackroom"]["items"].append(Item("Carrot", "Restores 10 hit points."))

def use(self, item_name):
    for item in self.inventory:
        if item.name == item_name:
            if item_name == "Carrot":
                self.hp += 10
                self.inventory.remove(item)
                print(f"🧪 You use the {item_name}. You now have {self.hp} HP.")
            else:
                print(f"🤷 You can't do anything with the {item_name} here.")
            return
    print(f"❓ You don't have a '{item_name}' in your bag.")

Player.use = use

hero = Player("Ben", "tackroom")
hero.hp = 5
hero.take("Carrot")
hero.use("Carrot")
hero.use("Carrot")