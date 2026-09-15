# Schritt 1: Steckbrief-Dictionary
steckbrief = {
    "name": "Captain Zara",
    "rang": "Kommandantin",
    "abteilung": "Führung",
    "spezialitaet": "Taktik & Navigation"
}
print("=== Steckbrief ===")
for k, v in steckbrief.items():
    print(f"  {k}: {v}")

# Schritt 2: Crew-Liste
crew_liste = [
    {"name": "Captain Zara", "rang": "Kommandantin", "abteilung": "Führung", "spezialitaet": "Taktik"},
    {"name": "Dr. Orion", "rang": "Arzt", "abteilung": "Medizin", "spezialitaet": "Xenobiologie"},
    {"name": "Tech Maya", "rang": "Ingenieurin", "abteilung": "Technik", "spezialitaet": "Antrieb"},
]

print("\n=== Alle Steckbriefe ===")
for m in crew_liste:
    print(f"  {m['name']} – {m['rang']} ({m['spezialitaet']})")