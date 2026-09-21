def berechne_credits(auftraege, pro_auftrag):
    return auftraege * pro_auftrag

credits = berechne_credits(5, 40)
print(f"Cyber Credits: {credits}")
