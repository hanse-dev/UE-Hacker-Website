eintraege = ["Hafer-1", "Heu-2", "Hafer-3", "Müsli-4"]
def filtere_eintraege(liste, suchbegriff):
    treffer = []
    for eintrag in liste:
        if suchbegriff in eintrag:
            treffer.append(eintrag)
    return treffer

ergebnis = filtere_eintraege(eintraege, "Hafer")
print(ergebnis)
print(f"Treffer: {len(ergebnis)}")
