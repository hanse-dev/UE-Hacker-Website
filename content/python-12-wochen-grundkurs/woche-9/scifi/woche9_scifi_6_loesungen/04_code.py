# Problem: Kann nicht im 'w' Modus lesen
with open('test.txt', 'w') as f:
    f.write('Hallo')

with open('test.txt', 'r') as f:
    inhalt = f.read()
    print(f'Inhalt: {inhalt}')