eingabe = "zehn"
try:
    zahl = int(eingabe)
except ValueError:
    zahl = 0
print(f"Zahl: {zahl}")
