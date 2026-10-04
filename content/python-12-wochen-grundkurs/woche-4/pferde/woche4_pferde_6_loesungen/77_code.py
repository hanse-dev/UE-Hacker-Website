energie = 100
runde = 0
while runde < 6:
    runde += 1
    energie -= 15
    if runde == 3:
        energie += 20
    print(f"Runde {runde}: Energie {energie}")
