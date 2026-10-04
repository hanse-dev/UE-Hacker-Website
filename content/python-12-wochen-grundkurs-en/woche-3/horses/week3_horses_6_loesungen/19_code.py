hay_stock = 45
need = 50
if hay_stock >= need:
    print("Enough hay!")
else:
    print(f"Not enough hay! Missing: {need - hay_stock} kg")
