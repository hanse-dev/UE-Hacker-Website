# ⚔️ Evolution Spell 4: Polymorphism

**Polymorphism** means "many forms": you call **the same method** on very different objects – each reacts **in its own way**:

```python
team = [Hero("Luna"), Warrior("Aria"), Mage("Thorin")]
for f in team:
    f.fight()
```

1. All three objects have `fight()`, but every class does something different
2. The loop does **not need to know** which class is next
3. **Duck typing:** "If it walks like a duck and quacks like a duck, it is a duck." A class **without** inheritance may join in as well if it has the method.
