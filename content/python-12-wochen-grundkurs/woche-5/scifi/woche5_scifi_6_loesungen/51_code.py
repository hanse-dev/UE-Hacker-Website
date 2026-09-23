def ist_wartbar(energie, dauer):
    return energie >= dauer * 2

print(f"Nebula: {ist_wartbar(90, 40)}")
print(f"Comet: {ist_wartbar(60, 40)}")
