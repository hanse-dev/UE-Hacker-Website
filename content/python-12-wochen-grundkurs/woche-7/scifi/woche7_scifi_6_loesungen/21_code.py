from datetime import datetime

jetzt = datetime.now()
print(f"Stunde gültig: {0 <= jetzt.hour <= 23}")
print(f"Jahr hat 4 Stellen: {len(jetzt.strftime('%Y')) == 4}")
