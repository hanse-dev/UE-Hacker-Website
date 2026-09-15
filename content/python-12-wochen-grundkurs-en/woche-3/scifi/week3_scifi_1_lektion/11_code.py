# Example 1: and – both conditions must be true
has_access_code = True
has_fingerprint = True
if has_access_code and has_fingerprint:
    print("🔐👆 Access to the command deck granted!")

# Example 2: or – one condition is enough
has_emergency_key = False
has_override_code = True
if has_emergency_key or has_override_code:
    print("🔓 You can open the door manually!")

# Example 3: not – flips a truth value
alarm_active = False
if not alarm_active:
    print("✅ No danger – all systems secure!")