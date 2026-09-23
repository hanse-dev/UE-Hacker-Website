def berechne_vorrat(crew, tage):
    gesamt = crew * tage
    return gesamt

vorrat = berechne_vorrat(7, 3)
print(f"Vorrat: {vorrat}")
