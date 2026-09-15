# Beispiel 4: For-Schleife über einen String
print("=== Beispiel 4: Buchstaben eines Codes ===")
code = "ALPHA"
print(f"Der Code ist: {code}")
print("Buchstaben für Buchstabe:")

for buchstabe in code:
    print(f"  - {buchstabe}")

print("\n=== Was passiert hier? ===")
print("String wird als Sequenz von Buchstaben behandelt")
print("Jeder Buchstabe wird einzeln durchlaufen")