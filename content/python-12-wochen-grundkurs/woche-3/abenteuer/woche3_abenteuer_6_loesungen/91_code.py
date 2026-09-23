phase1_ok = True
phase2_ok = True
phase3_ok = False
phase4_ok = True
phase5_ok = True
gefahrenstufe = 4

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

if erfolgreiche_phasen >= 4 and gefahrenstufe <= 3:
    print("Quest bestanden!")
else:
    print("Quest gescheitert!")
