# Beispiel 1: and – beide Bedingungen müssen stimmen
hat_schluessel = True
hat_fackel = True
if hat_schluessel and hat_fackel:
    print("🗝️🔥 Du kannst die dunkle Kammer sicher öffnen!")

# Beispiel 2: or – eine Bedingung reicht
hat_schwert = False
hat_zauberstab = True
if hat_schwert or hat_zauberstab:
    print("⚔️ Du bist bewaffnet und bereit!")

# Beispiel 3: not – kehrt einen Wahrheitswert um
ist_verflucht = False
if not ist_verflucht:
    print("✨ Du bist frei von jedem Fluch!")