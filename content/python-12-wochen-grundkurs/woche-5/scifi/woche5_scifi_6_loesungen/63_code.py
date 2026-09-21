def reicht_treibstoff(bedarf, vorrat):
    return vorrat >= bedarf

print(f"Reicht: {reicht_treibstoff(280, 300)}")
print(f"Reicht: {reicht_treibstoff(280, 200)}")
