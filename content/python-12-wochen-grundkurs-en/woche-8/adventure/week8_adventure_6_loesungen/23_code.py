artifact = ("Fire staff", 15, "Fire")
try:
    artifact[1] = 99
except TypeError:
    print("Error: protected")
