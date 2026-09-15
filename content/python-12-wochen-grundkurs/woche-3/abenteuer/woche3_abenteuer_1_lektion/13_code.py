# Beispiel: Die verschlossene Tür
tuer_verschlossen = True
richtiger_schluessel = True

if tuer_verschlossen:
    print("🚪 Die Tür ist verschlossen.")
    if richtiger_schluessel:
        print("🔑 Der Schlüssel passt – die Tür öffnet sich!")
    else:
        print("❌ Dieser Schlüssel passt nicht.")
else:
    print("🚪 Die Tür steht bereits offen.")