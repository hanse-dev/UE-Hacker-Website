# Beispiel 1: and – beide Bedingungen müssen stimmen
hat_sattel = True
hat_helm = True
if hat_sattel and hat_helm:
    print("🐎🪖 Du bist bereit zum Reiten!")

# Beispiel 2: or – eine Bedingung reicht
hat_trense = False
hat_halfter = True
if hat_trense or hat_halfter:
    print("🐴 Du kannst das Pferd führen!")

# Beispiel 3: not – kehrt einen Wahrheitswert um
ist_krank = False
if not ist_krank:
    print("💪 Das Pferd ist gesund und einsatzbereit!")