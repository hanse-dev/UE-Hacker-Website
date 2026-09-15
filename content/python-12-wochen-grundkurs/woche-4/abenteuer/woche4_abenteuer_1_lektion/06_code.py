# Beispiel 4: For-Schleife über einen String
print("=== Beispiel 4: Buchstaben eines Namens ===")
name = "Aria"
print(f"Der Name ist: {name}")
print("Buchstaben für Buchstabe:")

for buchstabe in name:
    print(f"  - {buchstabe}")

print("\n=== Was passiert hier? ===")
print("String wird als Sequenz von Buchstaben behandelt")
print("Jeder Buchstabe wird einzeln durchlaufen")