# Example 2: Removing elements
feed_plan = ["Hay", "Oats", "Muesli", "Carrots", "Apples", "Muesli"]
print(f"Original feed plan: {feed_plan}")

# Remove the first occurrence with remove()
feed_plan.remove("Muesli")
print(f"After remove('Muesli'): {feed_plan}")

# Remove and return the last element with pop()
last_feed = feed_plan.pop()
print(f"After pop(): {feed_plan}")
print(f"Removed feed: {last_feed}")

# Remove a specific element with pop(index)
second_feed = feed_plan.pop(1)
print(f"After pop(1): {feed_plan}")
print(f"Removed feed: {second_feed}")

# Clear everything with clear()
feed_plan.clear()
print(f"After clear(): {feed_plan}")