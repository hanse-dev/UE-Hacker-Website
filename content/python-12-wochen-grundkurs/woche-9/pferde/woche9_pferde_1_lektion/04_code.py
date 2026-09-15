# Beispiel 2: Zeilenweiser Zugriff
# Mehrere Daten speichern
pferde_daten = [
    'Thunder,Hannoveraner,8,1.72\n',
    'Luna,Isländer,6,1.35\n',
    'Stormy,Quarter Horse,10,1.58\n'
]

with open('pferde_liste.txt', 'w') as f:
    f.writelines(pferde_daten)

print('✅ Pferde-Liste gespeichert!')

# Zeilenweise lesen
with open('pferde_liste.txt', 'r') as f:
    print('=== Pferde-Daten ===')
    for zeile in f:
        daten = zeile.strip().split(',')
        print(f'Name: {daten[0]}, Rasse: {daten[1]}, Alter: {daten[2]}, Größe: {daten[3]}m')