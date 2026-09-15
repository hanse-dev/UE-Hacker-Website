# Example 2: Removing elements
system_protocols = ["Alpha", "Beta", "Gamma", "Delta", "Epsilon", "Gamma"]
print(f"Original protocols: {system_protocols}")

# Remove first occurrence with remove()
system_protocols.remove("Gamma")
print(f"After remove('Gamma'): {system_protocols}")

# Remove and return last element with pop()
last_protocol = system_protocols.pop()
print(f"After pop(): {system_protocols}")
print(f"Removed protocol: {last_protocol}")

# Remove specific element with pop(index)
second_protocol = system_protocols.pop(1)
print(f"After pop(1): {system_protocols}")
print(f"Removed protocol: {second_protocol}")

# Delete everything with clear()
system_protocols.clear()
print(f"After clear(): {system_protocols}")