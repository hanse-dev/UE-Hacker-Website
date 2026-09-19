schutz = 80
angriff = 60
heilung = 20

if schutz >= 50:
    if angriff >= 50:
        if heilung >= 50:
            print("Magieprüfung bestanden")
        else:
            print("Heilung zu schwach")
    else:
        print("Angriff zu schwach")
else:
    print("Schutz zu schwach")
