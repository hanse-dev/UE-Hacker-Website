def total_cost(price, amount):
    return price * amount

total = total_cost(15, 4)
gold = 100 - total
print(f"Gold left: {gold}")
