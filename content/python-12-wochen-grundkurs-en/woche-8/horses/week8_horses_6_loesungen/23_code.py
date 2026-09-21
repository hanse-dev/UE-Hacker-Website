gear = ("Saddle", 15, "Leather")
try:
    gear[1] = 99
except TypeError:
    print("Error: protected")
