def berechne_leben(level, klasse):
    if klasse == "Krieger":
        return level * 20
    else:
        return level * 10

print(f"Krieger: {berechne_leben(3, 'Krieger')}")
print(f"Magier: {berechne_leben(3, 'Magier')}")
