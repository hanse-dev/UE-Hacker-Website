"""## 📚 Daten-Stream 1: Der Datei-Zugriff - Das digitale Tor

**Was es ist:** Der Datei-Zugriff ermöglicht dir, Daten auf der Festplatte zu speichern und zu laden.

**So funktioniert der Datei-Zugriff:**
```python
# Datei öffnen und schreiben
with open('datei.txt', 'w') as f:
    f.write('Hallo Welt')

# Datei öffnen und lesen
with open('datei.txt', 'r') as f:
    inhalt = f.read()
```

**Schritt-für-Schritt-Erklärung:**
1. **`open()`** - Funktion zum Öffnen von Dateien
2. **`'w'/'r'`** - Modus: schreiben/lesen
3. **`with`** - Kontextmanager für sicheren Zugriff
4. **`f.write()`/`f.read()`** - Schreiben/Lesen

**Warum so nützlich:**
- 🎯 Daten dauerhaft speichern
- 🔍 Große Datenmengen verarbeiten
- ⚡ Automatische Ressourcenverwaltung
- 🎲 Verschiedene Dateiformate unterstützen"""
