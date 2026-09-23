from datetime import datetime

stunde = datetime.now().hour
if 6 <= stunde <= 17:
    tageszeit = "Tag"
else:
    tageszeit = "Nacht"
print(f"Tageszeit gültig: {tageszeit in ['Tag', 'Nacht']}")
