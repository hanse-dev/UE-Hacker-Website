def berechne_leben(monster_anzahl):
    return (monster_anzahl + 1) // 2

print(f"Leben: {berechne_leben(5)}")
print(f"Leben: {berechne_leben(4)}")
print(f"Leben: {berechne_leben(0)}")
