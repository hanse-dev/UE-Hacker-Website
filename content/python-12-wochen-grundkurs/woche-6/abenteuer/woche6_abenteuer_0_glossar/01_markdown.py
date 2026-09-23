"""# 📖 Glossar – 🗡️ Woche 6 – Listen: Die Schatzkammer der Sammlungen
> Dieses Notebook kannst du die ganze Woche offen lassen.

| Begriff | Bedeutung | Beispiel |
|---------|-----------|----------|
| **Liste** `[]` | Geordnete Sammlung von Werten | `[\"Aria\", \"Borin\", \"Lena\"]` |
| `.append()` | Element am Ende der Liste hinzufügen | `liste.append(\"neu\")` |
| **Index** | Position eines Elements in der Liste (beginnt bei 0) | `liste[0]` → erstes Element |
| `len()` | Anzahl der Elemente in einer Liste | `len([1, 2, 3])` → `3` |
| `.insert()` | Element an einer bestimmten Position einfügen | `liste.insert(1, \"x\")` |
| `.remove()` | Erstes Vorkommen eines Elements entfernen | `liste.remove(\"x\")` |
| `.pop()` | Letztes (oder ein bestimmtes) Element entfernen und zurückgeben | `liste.pop()` |
| `.index()` | Position eines Elements finden | `liste.index(\"x\")` |
| `.count()` | Wie oft ein Element vorkommt | `liste.count(\"x\")` |
| `in` | Prüfen ob ein Element in der Liste vorhanden ist | `\"x\" in liste` |
| `.sort()` | Liste aufsteigend sortieren (verändert die Liste) | `liste.sort()` |
| `sorted()` | Gibt eine sortierte Kopie zurück (Original bleibt) | `sorted(liste)` |
| `.reverse()` | Reihenfolge der Liste umkehren | `liste.reverse()` |
| `enumerate()` | Index und Wert gleichzeitig beim Durchlaufen | `for i, x in enumerate(liste):` |
| `break` | Schleife sofort beenden | `if x == 5: break` |
| `continue` | Aktuelle Runde überspringen, mit nächster weitermachen | `if x == 0: continue` |
| `set` | Menge – wie Liste, aber ohne Duplikate und ohne feste Reihenfolge | `set([1,1,2])` → `{1, 2}` |
| **Algorithmus** | Schritt-für-Schritt-Lösungsweg – wie ein Kochrezept für den Computer | `for x in liste: if x > max: max = x` |
| **List Comprehension** | Kurzschreibweise, um aus einer Liste eine neue zu erzeugen | `[x for x in liste if x > 5]` |"""