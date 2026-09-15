alter = 15

# if / elif / else
if alter >= 18:
    print("Erwachsen")
elif alter >= 13:
    print("Teenager")
else:
    print("Kind")

# Vergleichsoperatoren
print(alter == 15)   # True
print(alter != 10)   # True
print(alter > 10)    # True

# Logische Operatoren
print(alter > 10 and alter < 20)  # True
print(alter < 10 or alter > 12)   # True
