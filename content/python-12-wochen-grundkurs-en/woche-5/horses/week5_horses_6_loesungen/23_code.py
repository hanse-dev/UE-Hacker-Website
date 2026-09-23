def is_ready(fitness):
    if fitness >= 70:
        return True
    return False

print(is_ready(80))
print(is_ready(50))
