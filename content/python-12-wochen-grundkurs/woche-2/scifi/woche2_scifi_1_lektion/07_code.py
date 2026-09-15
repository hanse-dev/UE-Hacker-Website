# Beispiel 1: Mathematische Operationen
planeten_a = 8
planeten_b = 4
print(f"Gesamtplaneten: {planeten_a + planeten_b}")
print(f"Differenz: {planeten_a - planeten_b}")
print(f"Verdopplung: {planeten_a * 2}")
print(f"Pro Sektor: {planeten_a / 2}")

# Beispiel 2: String-Operationen
prefix = "Neo"
suffix = "tron"
system_name = prefix + suffix
print(f"Systemname: {system_name}")
print(f"Signal: {prefix * 3}")

# Beispiel 3: Datentransformation
temperatur_str = "273"
temperatur_int = int(temperatur_str)
print(f"Temperatur als Text: {temperatur_str}K (Typ: {type(temperatur_str)})")
print(f"Temperatur als Zahl: {temperatur_int}K (Typ: {type(temperatur_int)})")

# Beispiel 4: Sensordaten verarbeiten
# Sensor-Eingabe simuliert (später mit input())
sensor_wert = "42.5"
wert_float = float(sensor_wert)
print(f"Sensorwert {wert_float} verdoppelt: {wert_float * 2}")