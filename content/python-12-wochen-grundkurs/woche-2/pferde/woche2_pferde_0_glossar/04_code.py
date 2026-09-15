pferd = "Bobby"
alter = 5

# f-String – Variable direkt im Text
print(f"Pferd: {pferd}, Alter: {alter}")

# type() – Typ prüfen
print(type(pferd))    # <class 'str'>
print(type(alter))    # <class 'int'>

# len() – Länge
print(len(pferd))     # 5

# String-Methoden
print(pferd.upper())  # BOBBY
print(pferd.lower())  # bobby
