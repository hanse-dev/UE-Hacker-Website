def create_stall(stall_id, size):
    return {"id": stall_id, "size": size, "feed": 0}

stalls = [
    create_stall("Stall-1", 3),
    create_stall("Stall-2", 2),
    create_stall("Stall-3", 4),
]

def distribute_feed(stalls, total_feed):
    total_size = sum(s["size"] for s in stalls)
    for s in stalls:
        s["feed"] = round(total_feed * s["size"] / total_size, 1)

distribute_feed(stalls, 90)

def plan_stable_shifts(num_riders, shifts):
    per_shift = num_riders // shifts
    remainder = num_riders % shifts
    return [per_shift + (1 if i < remainder else 0) for i in range(shifts)]

shifts = plan_stable_shifts(10, 2)

def generate_stable_report(stalls, total_feed, riders_per_shift):
    report = "=== STABLE REPORT ===\n"
    for s in stalls:
        report += f"  {s['id']}: Size {s['size']}, Feed {s['feed']} kg\n"
    report += f"Total feed: {total_feed} kg\n"
    report += f"Riders per shift: {riders_per_shift}"
    return report

print(generate_stable_report(stalls, 90, shifts))

def check_feed(stall, min_feed=15):
    if stall["feed"] < min_feed:
        return f"WARNING: {stall['id']} has only {stall['feed']} kg feed!"
    return None

for s in stalls:
    warning = check_feed(s)
    if warning:
        print(warning)