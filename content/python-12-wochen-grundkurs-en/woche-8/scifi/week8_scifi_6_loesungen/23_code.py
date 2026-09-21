part = ("Shield module", 15, "Energy")
try:
    part[1] = 99
except TypeError:
    print("Error: protected")
