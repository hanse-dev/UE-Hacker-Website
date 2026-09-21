eintraege = ["Chip-1", "Kabel-2", "Chip-3", "Modul-4"]
def filtere_eintraege(liste, suchbegriff):
    treffer = []
    for eintrag in liste:
        if suchbegriff in eintrag:
            treffer.append(eintrag)
    return treffer

ergebnis = filtere_eintraege(eintraege, "Chip")
print(ergebnis)
print(f"Treffer: {len(ergebnis)}")
