# Sensor arrays as a dictionary of dictionaries
sensors = {
    "Long-Range Radar": {"technician": "Lt. Vex", "status": "active", "range": 100},
    "Short-Range Scanner": {"technician": "Ens. Pryn", "status": "maintenance", "range": 60},
    "Spectral Analyzer": {"technician": "Dr. Aiko", "status": "active", "range": 85},
}

print("=== Sensor Matrix ===")
for name, data in sensors.items():
    symbol = "✅" if data["status"] == "active" else "⚠️"
    print(f"  {symbol} {name}: Technician: {data['technician']}, Range: {data['range']}%")

# Arrays needing maintenance
needs_maintenance = {k: v for k, v in sensors.items() if v["range"] < 80}
print(f"\nArrays needing maintenance: {list(needs_maintenance.keys())}")

# Average range
avg = sum(v["range"] for v in sensors.values()) / len(sensors)
print(f"Average range: {avg:.1f}%")
