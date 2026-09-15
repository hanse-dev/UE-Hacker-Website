# Beispiel 1: and – beide Bedingungen müssen stimmen
hat_zugangscode = True
hat_fingerabdruck = True
if hat_zugangscode and hat_fingerabdruck:
    print("🔐👆 Zugang zum Kommandodeck gewährt!")

# Beispiel 2: or – eine Bedingung reicht
hat_notfallschluessel = False
hat_ueberbrueckungscode = True
if hat_notfallschluessel or hat_ueberbrueckungscode:
    print("🔓 Du kannst die Tür manuell öffnen!")

# Beispiel 3: not – kehrt einen Wahrheitswert um
alarm_aktiv = False
if not alarm_aktiv:
    print("✅ Keine Gefahr – alle Systeme sicher!")