def create_entry(material, number):
    return f"{material}-{number}"

catalog = []
for number in range(1, 11):
    catalog.append(create_entry("Oats", number))
print(f"Count: {len(catalog)}")
print(catalog[-1])
