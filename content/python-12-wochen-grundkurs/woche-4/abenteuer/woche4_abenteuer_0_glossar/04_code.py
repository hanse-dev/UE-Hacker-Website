# for-Schleife über eine Liste
helden = ["Aria", "Borin", "Lena"]
for held in helden:
    print("Held:", held)

# range() – Zahlenfolge
for i in range(3):
    print("Runde", i)

# while-Schleife
leben = 3
while leben > 0:
    print("Leben:", leben)
    leben = leben - 1

# Listen-Grundlagen
truppe = []
truppe.append("Magier")
truppe.append("Krieger")
print(truppe[0])   # Magier
print(len(truppe)) # 2
