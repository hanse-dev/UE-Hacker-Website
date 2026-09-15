def erstelle_boxen(anzahl_boxen, pferde_pro_box):
    return [["frei"] * pferde_pro_box for _ in range(anzahl_boxen)]

def pferd_einweisen(boxen, box_nr, platz_nr, pferd):
    boxen[box_nr][platz_nr] = pferd
    return boxen

stall = erstelle_boxen(4, 3)
stall = pferd_einweisen(stall, 0, 0, "Thunder")
stall = pferd_einweisen(stall, 0, 1, "Luna")
stall = pferd_einweisen(stall, 1, 0, "Storm")

print("=== Stall-Übersicht ===")
for i, box in enumerate(stall):
    print(f"Box {i+1}: {box}")

freie = sum(p == "frei" for box in stall for p in box)
print(f"Freie Plätze: {freie}")