def kampfrunde(leben, schaden):
    neues_leben = leben - schaden
    if neues_leben < 0:
        return 0
    return neues_leben

leben = 100
leben = kampfrunde(leben, 25)
print(f"Leben: {leben}")
leben = kampfrunde(leben, 25)
print(f"Leben: {leben}")
