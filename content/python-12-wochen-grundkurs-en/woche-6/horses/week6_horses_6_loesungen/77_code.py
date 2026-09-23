entries = ["Oats-1", "Hay-2", "Oats-3", "Muesli-4"]
def filter_entries(items, term):
    hits = []
    for entry in items:
        if term in entry:
            hits.append(entry)
    return hits

result = filter_entries(entries, "Oats")
print(result)
print(f"Hits: {len(result)}")
