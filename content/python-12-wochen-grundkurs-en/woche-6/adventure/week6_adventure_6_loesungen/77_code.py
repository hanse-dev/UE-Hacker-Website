entries = ["Gold-1", "Silver-2", "Gold-3", "Crystal-4"]
def filter_entries(items, term):
    hits = []
    for entry in items:
        if term in entry:
            hits.append(entry)
    return hits

result = filter_entries(entries, "Gold")
print(result)
print(f"Hits: {len(result)}")
