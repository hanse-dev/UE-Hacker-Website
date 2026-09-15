# Example 1: and – both conditions must be true
has_key = True
has_torch = True
if has_key and has_torch:
    print("🗝️🔥 You can safely open the dark chamber!")

# Example 2: or – one condition is enough
has_sword = False
has_wand = True
if has_sword or has_wand:
    print("⚔️ You are armed and ready!")

# Example 3: not – flips a truth value
is_cursed = False
if not is_cursed:
    print("✨ You are free of any curse!")