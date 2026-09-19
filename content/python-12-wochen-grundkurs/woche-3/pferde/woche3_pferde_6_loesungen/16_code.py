heu_vorrat = 45
bedarf = 50

if heu_vorrat >= bedarf:
    print("Genug Heu!")
else:
    print(f"Zu wenig Heu! Fehlt: {bedarf - heu_vorrat} kg")
