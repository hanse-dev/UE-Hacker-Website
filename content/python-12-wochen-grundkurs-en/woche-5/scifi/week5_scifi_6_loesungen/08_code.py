# Problem: missing return
def add_sensor_data(data1, data2):
    total = data1 + data2
    return total  # This was missing!

total_data = add_sensor_data(100, 250)
print(f"Total sensor data: {total_data}")  # Now prints 350!