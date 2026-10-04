novanet_genauigkeit = 0.92
deepcore_genauigkeit = 0.88
minimind_genauigkeit = 0.75
durchschnitt_genauigkeit = 0.85
ueber_1 = novanet_genauigkeit > durchschnitt_genauigkeit
ueber_2 = deepcore_genauigkeit > durchschnitt_genauigkeit
ueber_3 = minimind_genauigkeit > durchschnitt_genauigkeit
print(f"MiniMind über Durchschnitt: {ueber_3}")
