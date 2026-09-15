# ✨ Beispiele für gute und schlechte Namen

# ✅ Gute Namen (klar und beschreibend)
def berechne_futter_menge(gewicht, aktivitaet):
    """Berechnet die tägliche Futtermenge."""
    return gewicht * aktivitaet * 0.02

def finde_bestes_training(pferde_liste):
    """Findet das beste Training für eine Pferdeliste."""
    return max(pferde_liste)

def ist_pferd_verfuegbar(pferd_id, zeitpunkt):
    """Prüft, ob ein Pferd verfügbar ist."""
    return pferd_id not in belegte_pferde[zeitpunkt]

# ❌ Schlechte Namen (unklar oder falsche Konvention)
# def berechneFutterMenge():  # CamelCase
# def fm(g, a):  # Zu kurz, nicht beschreibend
# def feeding_calculation():  # Substantiv zuerst

print("=== Gute Funktionsnamen in Aktion ===")
futter = berechne_futter_menge(500, 1.5)
print(f"Futtermenge: {futter} kg")

trainings = ["Dressur", "Springen", "Western"]
bestes_training = finde_bestes_training(trainings)
print(f"Bestes Training: {bestes_training}")

# Beispiel-Daten für Verfügbarkeitsprüfung
belegte_pferde = {"morgen": ["Thunder", "Luna"], "mittag": []}
verfuegbar = ist_pferd_verfuegbar("Storm", "morgen")
print(f"Pferd verfügbar: {verfuegbar}")