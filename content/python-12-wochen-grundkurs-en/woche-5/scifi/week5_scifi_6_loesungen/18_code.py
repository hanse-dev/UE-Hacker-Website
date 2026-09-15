def generate_protocol_name(system_type, security_level):
    return f"{system_type.upper()}-L{security_level}"

def calculate_efficiency(complexity, system_type):
    factors = {"Alarm": 1.5, "Scan": 1.2, "Log": 0.9, "Backup": 1.0}
    factor = factors.get(system_type, 1.0)
    return min(100, int(complexity * factor * 8))

def create_protocol(system_type, security_level, complexity):
    name = generate_protocol_name(system_type, security_level)
    efficiency = calculate_efficiency(complexity, system_type)
    return {"name": name, "type": system_type, "level": security_level, "efficiency": efficiency}

protocols = []

def save_protocol(list_, protocol):
    list_.append(protocol)

save_protocol(protocols, create_protocol("Alarm", 3, 7))
save_protocol(protocols, create_protocol("Scan", 1, 4))
save_protocol(protocols, create_protocol("Log", 2, 5))
save_protocol(protocols, create_protocol("Backup", 4, 6))
save_protocol(protocols, create_protocol("Alarm", 5, 9))

print("=== PROTOCOL DATABASE ===")
for p in protocols:
    print(f"{p['name']} – Type: {p['type']}, Level: {p['level']}, Efficiency: {p['efficiency']}%")

total = sum(p["efficiency"] for p in protocols)
print(f"\nProtocol count: {len(protocols)}")
print(f"Average efficiency: {total // len(protocols)}%")

print("\n--- Sorted by efficiency ---")
for p in sorted(protocols, key=lambda x: x["efficiency"], reverse=True):
    print(f"  {p['name']}: {p['efficiency']}%")