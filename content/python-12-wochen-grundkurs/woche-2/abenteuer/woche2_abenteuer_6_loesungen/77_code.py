zauber1 = "Feuerball"
staerke1 = 80.0
komplex1 = 3
zauber2 = "Frostblitz"
staerke2 = 65.0
komplex2 = 2
zauber3 = "Sturmruf"
staerke3 = 95.0
komplex3 = 5

durchschnitt = (staerke1 + staerke2 + staerke3) / 3
maechtig = staerke3 > durchschnitt
print(f"Sturmruf mächtig: {maechtig}")
