# Example 1: and – both conditions must be true
has_saddle = True
has_helmet = True
if has_saddle and has_helmet:
    print("🐎🪖 You are ready to ride!")

# Example 2: or – one condition is enough
has_bridle = False
has_halter = True
if has_bridle or has_halter:
    print("🐴 You can lead the horse!")

# Example 3: not – flips a truth value
is_sick = False
if not is_sick:
    print("💪 The horse is healthy and ready to work!")