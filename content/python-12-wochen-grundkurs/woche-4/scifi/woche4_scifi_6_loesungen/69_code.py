spieler_reihe = 1
spieler_spalte = 1
ziel_reihe = 8
ziel_spalte = 8
while spieler_reihe < 8:
    spieler_reihe += 1
    spieler_spalte += 1
if spieler_reihe == ziel_reihe and spieler_spalte == ziel_spalte:
    print("🎯 Ziel erreicht!")
