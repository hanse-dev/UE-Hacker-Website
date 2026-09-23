entries = ["Chip-1", "Cable-2", "Chip-3", "Module-4"]
def filter_entries(items, term):
    hits = []
    for entry in items:
        if term in entry:
            hits.append(entry)
    return hits

result = filter_entries(entries, "Chip")
print(result)
print(f"Hits: {len(result)}")
