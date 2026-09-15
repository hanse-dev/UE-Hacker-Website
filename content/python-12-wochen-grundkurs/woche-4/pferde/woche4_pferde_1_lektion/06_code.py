# Beispiel 4: For-Schleife über einen String
print("=== Beispiel 4: Buchstaben eines Pferdenamens ===")
name = "Thunder"
print(f"Der Pferdename ist: {name}")
print("Buchstaben für Buchstabe:")

for buchstabe in name:
    print(f"  - {buchstabe}")

print("\n=== Was passiert hier? ===")
print("String wird als Sequenz von Buchstaben behandelt")
print("Jeder Buchstabe wird einzeln durchlaufen")