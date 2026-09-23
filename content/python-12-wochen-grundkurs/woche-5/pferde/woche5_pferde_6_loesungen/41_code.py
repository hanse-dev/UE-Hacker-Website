def ist_platz_frei(boxen, pferde):
    return boxen >= pferde

print(f"Halle: {ist_platz_frei(12, 10)}")
print(f"Weide: {ist_platz_frei(5, 8)}")
