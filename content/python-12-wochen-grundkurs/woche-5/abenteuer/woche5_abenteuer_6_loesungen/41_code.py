def ist_zauber_moeglich(mana_kosten, aktuelles_mana):
    return aktuelles_mana >= mana_kosten

print(f"Feuerball: {ist_zauber_moeglich(30, 50)}")
print(f"Blitz: {ist_zauber_moeglich(40, 25)}")
