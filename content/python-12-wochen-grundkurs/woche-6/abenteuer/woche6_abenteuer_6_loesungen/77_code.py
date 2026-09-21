eintraege = ["Gold-1", "Silber-2", "Gold-3", "Kristall-4"]
def filtere_eintraege(liste, suchbegriff):
    treffer = []
    for eintrag in liste:
        if suchbegriff in eintrag:
            treffer.append(eintrag)
    return treffer

ergebnis = filtere_eintraege(eintraege, "Gold")
print(ergebnis)
print(f"Treffer: {len(ergebnis)}")
