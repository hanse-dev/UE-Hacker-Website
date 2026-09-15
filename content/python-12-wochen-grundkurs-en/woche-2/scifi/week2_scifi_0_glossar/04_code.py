ship = "Enterprise"
crew = 150

# f-String – variable directly in text
print(f"Ship: {ship}, Crew: {crew}")

# type() – check type
print(type(ship))   # <class 'str'>
print(type(crew))   # <class 'int'>

# len() – length
print(len(ship))    # 10

# String methods
print(ship.upper()) # ENTERPRISE
print(ship.lower()) # enterprise