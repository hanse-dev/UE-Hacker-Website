acc1 = 0.92
acc2 = 0.88
acc3 = 0.75
average_acc = 0.85
above_1 = acc1 > average_acc
above_2 = acc2 > average_acc
above_3 = acc3 > average_acc
print(f"NovaNet above average: {above_1}")
print(f"DeepCore above average: {above_2}")
print(f"MiniMind above average: {above_3}")
