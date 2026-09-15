# Step 1 – Create AI models (5)
ai1_name = "ARIA-7"
ai1_accuracy = 0.94
ai1_parameters = 7000000
ai1_training_time = 48

ai2_name = "NEXUS-3"
ai2_accuracy = 0.87
ai2_parameters = 2500000
ai2_training_time = 24

ai3_name = "QUANTUM-1"
ai3_accuracy = 0.98
ai3_parameters = 15000000
ai3_training_time = 96

ai4_name = "DELTA-9"
ai4_accuracy = 0.79
ai4_parameters = 1200000
ai4_training_time = 12

ai5_name = "SIGMA-X"
ai5_accuracy = 0.91
ai5_parameters = 5000000
ai5_training_time = 36

# Step 2 – Model descriptions
print("=== AI LAB PROTOCOL ===")
print(f"{ai1_name}: Accuracy {ai1_accuracy}, Parameters {ai1_parameters}, Training {ai1_training_time}h")
print(f"{ai2_name}: Accuracy {ai2_accuracy}, Parameters {ai2_parameters}, Training {ai2_training_time}h")
print(f"{ai3_name}: Accuracy {ai3_accuracy}, Parameters {ai3_parameters}, Training {ai3_training_time}h")
print(f"{ai4_name}: Accuracy {ai4_accuracy}, Parameters {ai4_parameters}, Training {ai4_training_time}h")
print(f"{ai5_name}: Accuracy {ai5_accuracy}, Parameters {ai5_parameters}, Training {ai5_training_time}h")
print()

# Step 3 – Sum parameters
total_params = ai1_parameters + ai2_parameters + ai3_parameters + ai4_parameters + ai5_parameters
print(f"Total parameters: {total_params}")

# Step 4 – Best and largest model
print(f"Most accurate model: {ai3_name} ({ai3_accuracy})")
print(f"Largest model: {ai3_name} ({ai3_parameters} parameters)")

# Step 5 – Average accuracy
total_accuracy = ai1_accuracy + ai2_accuracy + ai3_accuracy + ai4_accuracy + ai5_accuracy
average = total_accuracy / 5
print(f"Average accuracy: {average:.3f}")

# Step 6 – Boolean marking
ai1_strong = ai1_accuracy > average
ai2_strong = ai2_accuracy > average
ai3_strong = ai3_accuracy > average
ai4_strong = ai4_accuracy > average
ai5_strong = ai5_accuracy > average
print(f"{ai1_name} above average: {ai1_strong}")
print(f"{ai2_name} above average: {ai2_strong}")
print(f"{ai3_name} above average: {ai3_strong}")
print(f"{ai4_name} above average: {ai4_strong}")
print(f"{ai5_name} above average: {ai5_strong}")

# Bonus: efficiency
print()
print(f"Efficiency {ai1_name}: {ai1_accuracy / ai1_parameters * 1000000:.4f}")
print(f"Efficiency {ai2_name}: {ai2_accuracy / ai2_parameters * 1000000:.4f}")
print(f"Efficiency {ai3_name}: {ai3_accuracy / ai3_parameters * 1000000:.4f}")
print(f"Efficiency {ai4_name}: {ai4_accuracy / ai4_parameters * 1000000:.4f}")
print(f"Efficiency {ai5_name}: {ai5_accuracy / ai5_parameters * 1000000:.4f}")