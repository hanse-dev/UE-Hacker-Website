# Beispiel: Die verschlossene Stalltür
stalltuer_verschlossen = True
richtiger_schluessel = True

if stalltuer_verschlossen:
    print("🚪 Die Stalltür ist verschlossen.")
    if richtiger_schluessel:
        print("🔑 Der Schlüssel passt – die Stalltür öffnet sich!")
    else:
        print("❌ Dieser Schlüssel passt nicht.")
else:
    print("🚪 Die Stalltür steht bereits offen.")