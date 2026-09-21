regale = ["Regal der Elemente", "Regal der Tiere", "Regal der Sterne", "Regal der Schatten", "Regal der Helden"]
import random

gewaehlt = random.choice(regale)
print(f"Gewählt gültig: {gewaehlt in regale}")
