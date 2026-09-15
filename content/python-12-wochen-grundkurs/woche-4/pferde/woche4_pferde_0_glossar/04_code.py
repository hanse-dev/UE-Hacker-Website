# for-Schleife über eine Liste
pferde = ["Bobby", "Blitz", "Moritz"]
for pferd in pferde:
    print("Pferd:", pferd)

# range() – Zahlenfolge
for i in range(3):
    print("Runde", i)

# while-Schleife
futter = 3
while futter > 0:
    print("Futter:", futter, "kg")
    futter = futter - 1

# Listen-Grundlagen
stall = []
stall.append("Haflinger")
stall.append("Andalusier")
print(stall[0])   # Haflinger
print(len(stall)) # 2
