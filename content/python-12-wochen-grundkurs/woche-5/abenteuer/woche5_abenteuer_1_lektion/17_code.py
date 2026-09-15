# ✨ Beispiele für gute und schlechte Namen

# ✅ Gute Namen (klar und beschreibend)
def berechne_heilung(basis_heilung, multiplikator):
    """Berechnet die Heilungsmenge."""
    return basis_heilung * multiplikator

def finde_max_level(level_liste):
    """Findet das höchste Level in einer Liste."""
    return max(level_liste)

def ist_quest_verfuegbar(level, benoetigt_level):
    """Prüft, ob eine Quest verfügbar ist."""
    return level >= benoetigt_level

# ❌ Schlechte Namen (unklar oder falsche Konvention)
# def berechneHeilung():  # CamelCase
# def bs(b, m):  # Zu kurz, nicht beschreibend
# def healing_calculation():  # Substantiv zuerst

print("=== Gute Funktionsnamen in Aktion ===")
heilung = berechne_heilung(10, 2)
print(f"Heilung: {heilung}")

levels = [5, 8, 12, 3, 15]
max_level = finde_max_level(levels)
print(f"Höchstes Level: {max_level}")

quest_ok = ist_quest_verfuegbar(8, 10)
print(f"Quest verfügbar: {quest_ok}")