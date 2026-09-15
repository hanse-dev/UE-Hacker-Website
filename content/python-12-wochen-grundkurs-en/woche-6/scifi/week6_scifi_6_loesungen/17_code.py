def generate_dataset(data_type, complexity):
    base = ["A-01", "B-02", "C-03"]
    extended = ["D-04", "E-05", "F-06"]
    advanced = ["G-07", "H-08", "I-09"]
    data = [f"{data_type}-{entry}" for entry in base]
    if complexity >= 2:
        data += [f"{data_type}-{e}" for e in extended]
    if complexity >= 3:
        data += [f"{data_type}-{e}" for e in advanced]
    return data

ship_data = generate_dataset("Ship", 2)
mission_data = generate_dataset("Mission", 3)
print(f"Ship data: {ship_data}")
print(f"Mission data: {mission_data}")
filtered = [d for d in mission_data if "G" in d or "H" in d]
print(f"Filtered: {filtered}")