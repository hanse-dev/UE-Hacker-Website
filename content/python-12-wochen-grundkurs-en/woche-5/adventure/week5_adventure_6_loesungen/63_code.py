def is_affordable(costs, gold):
    return gold >= costs

print(f"Affordable: {is_affordable(150, 200)}")
print(f"Affordable: {is_affordable(150, 100)}")
