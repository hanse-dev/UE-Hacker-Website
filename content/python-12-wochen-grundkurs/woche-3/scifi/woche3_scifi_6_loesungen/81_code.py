phase1_ok = True
phase2_ok = True
phase3_ok = False
phase4_ok = True
phase5_ok = True
erfolgreiche_phasen = 0
if phase1_ok:
    erfolgreiche_phasen = erfolgreiche_phasen + 1
if phase2_ok:
    erfolgreiche_phasen = erfolgreiche_phasen + 1
if phase3_ok:
    erfolgreiche_phasen = erfolgreiche_phasen + 1
if phase4_ok:
    erfolgreiche_phasen = erfolgreiche_phasen + 1
if phase5_ok:
    erfolgreiche_phasen = erfolgreiche_phasen + 1
print(f"Erfolgreiche Phasen: {erfolgreiche_phasen}")