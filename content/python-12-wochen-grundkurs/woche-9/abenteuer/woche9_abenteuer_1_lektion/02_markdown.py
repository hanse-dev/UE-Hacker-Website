"""## 📚 Daten-Stream 1: Der Schriftrollen-Zugriff - Das magische Tor

**Was es ist:** Der Schriftrollen-Zugriff ermöglicht dir, Daten auf magischen Schriftrollen zu speichern und zu laden.

**So funktioniert der Schriftrollen-Zugriff:**
```python
# Schriftrolle öffnen und schreiben
with open('rolle.txt', 'w') as f:
    f.write('Hallo Pyralia')

# Schriftrolle öffnen und lesen
with open('rolle.txt', 'r') as f:
    inhalt = f.read()
```

**Schritt-für-Schritt-Erklärung:**
1. **`open()`** - Zauber zum Öffnen von Schriftrollen
2. **`'w'/'r'`** - Modus: schreiben/lesen
3. **`with`** - Magischer Kontext für sicheren Zugriff
4. **`f.write()`/`f.read()`** - Schreiben/Lesen

**Warum so nützlich:**
- 🎯 Daten dauerhaft auf Schriftrollen bewahren
- 🔍 Große Datenmengen verarbeiten
- ⚡ Automatische magische Verwaltung
- 🎲 Verschiedene Schriftrollen-Formate unterstützen"""
