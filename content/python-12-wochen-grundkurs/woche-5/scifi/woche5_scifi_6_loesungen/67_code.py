def berechne_tempo(basis, ballast):
    tempo = basis - ballast
    if tempo < 0:
        return 0
    return tempo

print(f"Tempo: {berechne_tempo(40, 15)}")
print(f"Tempo: {berechne_tempo(10, 30)}")
