genau1 = 92.0
genau2 = 85.0
genau3 = 78.0
param1 = 5000000
param2 = 12000000
param3 = 800000

gesamt = param1 + param2 + param3
durchschnitt = (genau1 + genau2 + genau3) / 3
nexus_besser = genau1 > durchschnitt
pulsar_besser = genau3 > durchschnitt
print(f"Gesamtparameter: {gesamt}")
print(f"Durchschnittsgenauigkeit: {durchschnitt}")
print(f"Nexus über Durchschnitt: {nexus_besser}")
print(f"Pulsar über Durchschnitt: {pulsar_besser}")