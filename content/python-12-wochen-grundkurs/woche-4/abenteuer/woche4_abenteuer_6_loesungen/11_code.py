# Schritt 1 – Alle Zahlen 1 bis 20
print("=== Alle Zahlen 1-20 ===")
for i in range(1, 21):
    print(f"Zahl: {i}")

# Schritt 2 – Nur gerade Zahlen
print()
print("=== Gerade Zahlen ===")
for i in range(2, 21, 2):
    print(f"Gerade: {i}")

# Schritt 2 – Rückwärts 20 bis 1
print()
print("=== Countdown ===")
for i in range(20, 0, -1):
    print(f"Countdown: {i}")

# Schritt 3 – Summe 1 bis 100
summe = 0
for i in range(1, 101):
    summe += i
print()
print(f"Summe von 1 bis 100: {summe}")

# Bonus – Multiplikationsdreieck
print()
print("=== Magische Quadrat-Tafel ===")
for i in range(1, 11):
    print(f"{i} × {i} = {i * i}")