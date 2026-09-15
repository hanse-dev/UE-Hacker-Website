# Beispiel 2: Zeilenweiser Zugriff
# Mehrere Daten speichern
crew_daten = [
    'Captain Alex,35,15\n',
    'Dr. Zara,28,8\n',
    'Lt. Nova,26,6\n'
]

with open('crew_liste.txt', 'w') as f:
    f.writelines(crew_daten)

print('✅ Crew-Liste gespeichert!')

# Zeilenweise lesen
with open('crew_liste.txt', 'r') as f:
    print('=== Crew-Mitglieder ===')
    for zeile in f:
        daten = zeile.strip().split(',')
        print(f'Name: {daten[0]}, Alter: {daten[1]}, Erfahrung: {daten[2]}')