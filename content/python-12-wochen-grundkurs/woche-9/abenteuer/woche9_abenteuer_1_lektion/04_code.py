# Beispiel 2: Zeilenweiser Zugriff
# Mehrere Daten speichern
helden_daten = [
    'Aria,Magierin,15,2500\n',
    'Thorin,Krieger,18,3200\n',
    'Luna,Schurkin,12,1800\n'
]

with open('helden_liste.txt', 'w') as f:
    f.writelines(helden_daten)

print('✅ Helden-Liste gespeichert!')

# Zeilenweise lesen
with open('helden_liste.txt', 'r') as f:
    print('=== Helden-Mitglieder ===')
    for zeile in f:
        daten = zeile.strip().split(',')
        print(f'Name: {daten[0]}, Klasse: {daten[1]}, Level: {daten[2]}, XP: {daten[3]}')