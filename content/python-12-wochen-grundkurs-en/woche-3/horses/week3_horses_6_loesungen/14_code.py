hay_stock = 45
need = 50
if hay_stock >= need:
    print(f"Enough hay! Leftover: {hay_stock - need} kg")
else:
    print(f"Not enough hay! Missing: {need - hay_stock} kg")