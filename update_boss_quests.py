#!/usr/bin/env python3
"""
Skript zur Aktualisierung aller Boss-Quests ab Woche 2
mit der neuen, detaillierten Struktur
"""

import os
import json
from pathlib import Path

def update_boss_quest_cell(cell_content, theme):
    """
    Aktualisiert eine Boss-Quest-Zelle mit der neuen Struktur
    """
    lines = cell_content.split('\n')
    new_lines = []
    i = 0
    
    while i < len(lines):
        line = lines[i]
        
        # Überschrift beibehalten
        if line.startswith('### ⭐⭐⭐'):
            new_lines.append(line)
            
            # Belohnung beibehalten
            if i + 1 < len(lines) and lines[i+1].startswith('**Belohnung:**'):
                new_lines.append(lines[i+1])
                i += 2
            else:
                i += 1
            
            # Story beibehalten
            if i < len(lines) and not lines[i].startswith('**Was du tun sollst:**'):
                new_lines.append(line)
                i += 1
            
            # "Was du tun sollst:" ersetzen
            if i < len(lines) and lines[i].startswith('**Was du tun sollst:**'):
                new_lines.append(lines[i])
                i += 1
                
                # Alte Aufgaben durch neue detaillierte ersetzen
                new_lines.extend(generate_detailed_tasks(theme))
                
                # Bonus-Challenge beibehalten
                while i < len(lines):
                    if lines[i].startswith('**Bonus-Challenge:**'):
                        new_lines.append(lines[i])
                        i += 1
                        break
                    i += 1
            else:
                new_lines.append(line)
                i += 1
        else:
            new_lines.append(line)
            i += 1
    
    return '\n'.join(new_lines)

def generate_detailed_tasks(theme):
    """
    Generiert detaillierte Aufgaben basierend auf dem Theme
    """
    # Theme-spezifische Aufgaben hier implementieren
    # Dies ist eine vereinfachte Version
    tasks = [
        "\n**1. [Hauptaufgabe 1]:**",
        "   - Erstelle eine Funktion für [spezifische Aufgabe]",
        "   - Die Funktion soll [konkrete Anforderung]",
        "   - Tipp: [Hinweis ohne Lösung]",
        "",
        "**2. [Hauptaufgabe 2]:**",
        "   - Schreibe eine Funktion, die [beschreibt was zu tun ist]",
        "   - Erstelle eine Validierungsfunktion für [Zweck]",
        "   - Behandle Fehler wenn [Fehlerfall]",
        "",
        "**3. [Hauptaufgabe 3]:**",
        "   - Erstelle eine [Datenstruktur] als Zwischenspeicher",
        "   - Schreibe Funktionen zum Hinzufügen und Holen von Daten",
        "   - Implementiere eine Funktion zum [Aktion]",
        "",
        "**4. [Hauptaufgabe 4]:**",
        "   - Filtere Daten nach [Bedingung 1]",
        "   - Filtere Daten nach [Bedingung 2]",
        "   - Kombiniere mehrere Filterbedingungen",
        "",
        "**5. [Hauptaufgabe 5]:**",
        "   - Speichere gefilterte Daten als [Format 1]",
        "   - Speichere gefilterte Daten als [Format 2]",
        "   - Erstelle automatische Dateinamen mit Zeitstempel",
        "",
        "**6. [Hauptaufgabe 6]:**",
        "   - Starte den [Prozess]",
        "   - Verarbeite Daten in Echtzeit",
        "   - Zeige Statistik der verarbeiteten Daten",
        "",
        "**Beispiel-Struktur:**",
        "```python",
        "# So könntest du beginnen:",
        "import time",
        "import json",
        "",
        "def funktion_name(parameter):",
        "    # Beschreibung was die Funktion tut",
        "    pass",
        "",
        "# ... weitere Funktionen hier",
        "",
        "# Hauptprogramm",
        "daten = []",
        "# Verarbeite Daten...",
        "```"
    ]
    
    return tasks

def process_notebook(file_path):
    """
    Verarbeitet ein Jupyter Notebook
    """
    with open(file_path, 'r', encoding='utf-8') as f:
        notebook = json.load(f)
    
    theme = 'scifi' if 'scifi' in file_path else ('abenteuer' if 'abenteuer' in file_path else 'pferde')
    
    # Finde und aktualisiere Boss-Quest-Zellen
    for cell in notebook['cells']:
        if cell['cell_type'] == 'markdown':
            content = ''.join(cell['source'])
            if 'Boss-Quest' in content or 'Finale Herausforderung' in content:
                if 'Was du tun sollst:' in content:
                    updated_content = update_boss_quest_cell(content, theme)
                    cell['source'] = updated_content
    
    # Speichere aktualisiertes Notebook
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(notebook, f, indent=2, ensure_ascii=False)
    
    print(f"✅ Aktualisiert: {file_path}")

def main():
    """
    Hauptfunktion zum Aktualisieren aller Notebooks
    """
    base_path = Path('content/python-12-wochen-grundkurs')
    
    # Wochen 2-9 verarbeiten
    for week in range(2, 10):
        week_path = base_path / f'woche-{week}'
        if week_path.exists():
            print(f"\n📚 Verarbeite Woche {week}...")
            
            # Alle drei Themen verarbeiten
            for theme in ['scifi', 'abenteuer', 'pferde']:
                notebook_path = week_path / f'woche{week}_{theme}.ipynb'
                if notebook_path.exists():
                    process_notebook(notebook_path)

if __name__ == '__main__':
    main()
    print("\n✨ Alle Boss-Quests wurden aktualisiert!")
