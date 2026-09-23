def total_price(price, amount):
    return price * amount

total = total_price(30, 3)
credits = 100 - total
print(f"Credits left: {credits}")
