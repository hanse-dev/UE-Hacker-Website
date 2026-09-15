def erstelle_hangars(anzahl_hangars, plaetze_pro_hangar):
    return [["frei"] * plaetze_pro_hangar for _ in range(anzahl_hangars)]

def shuttle_andocken(hangars, hangar, platz, shuttle):
    hangars[hangar][platz] = shuttle
    return hangars

hangars = erstelle_hangars(3, 4)
hangars = shuttle_andocken(hangars, 0, 0, "Falke")
hangars = shuttle_andocken(hangars, 0, 1, "Kolibri")
hangars = shuttle_andocken(hangars, 1, 0, "Sturmvogel")
hangars = shuttle_andocken(hangars, 2, 0, "Kometenjäger")

print("=== Hangar-Übersicht ===")
for i, hangar in enumerate(hangars):
    print(f"Hangar {i+1}: {hangar}")

frei = sum(s == "frei" for hangar in hangars for s in hangar)
print(f"Freie Plätze: {frei}")
