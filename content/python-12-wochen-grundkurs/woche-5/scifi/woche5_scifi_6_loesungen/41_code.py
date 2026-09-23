def ist_energie_ok(bedarf, vorrat):
    return vorrat >= bedarf

print(f"Antrieb: {ist_energie_ok(30, 50)}")
print(f"Waffen: {ist_energie_ok(40, 25)}")
