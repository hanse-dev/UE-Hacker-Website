# Example 1: Mathematical operations
planets_a = 8
planets_b = 4
print(f"Total planets: {planets_a + planets_b}")
print(f"Difference: {planets_a - planets_b}")
print(f"Doubled: {planets_a * 2}")
print(f"Per sector: {planets_a / 2}")

# Example 2: String operations
prefix = "Neo"
suffix = "tron"
system_name = prefix + suffix
print(f"System name: {system_name}")
print(f"Signal: {prefix * 3}")

# Example 3: Data transformation
temperature_str = "273"
temperature_int = int(temperature_str)
print(f"Temperature as text: {temperature_str}K (type: {type(temperature_str)})")
print(f"Temperature as number: {temperature_int}K (type: {type(temperature_int)})")

# Example 4: Process sensor data
# Sensor input simulated (later with input())
sensor_value = "42.5"
value_float = float(sensor_value)
print(f"Sensor value {value_float} doubled: {value_float * 2}")