"""## ⚔️ Stage 4: An enemy and a fight

*Knowledge from Weeks 7 + 11: modules and methods*

What would an emergency be without an opponent? We build a class `Enemy` with a method `is_defeated()` (Week 11). The module `random` (Week 7) rolls the damage.

**How a fight works:**
1. The player strikes: 1 to 6 damage – with the item `Cutter` **+3 bonus**
2. If the enemy is not defeated yet, it strikes back
3. A `while` loop (Week 4) repeats this until someone has no hit points left

Rooms without an enemy get the value `None` (= "nothing"). Without the welding torch, the fight gets pretty tight!"""