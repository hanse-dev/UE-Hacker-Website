"""## 🪞 Warum `self`? – Der Schlüssel zu deinen Pferden

**Was ist `self`?** `self` ist die Referenz auf **das konkrete Pferd**, das gerade angesprochen wird. Wenn du `lucky.wiehern()` aufrufst, ist `self` in der Methode genau das Objekt `lucky`.

**Warum brauchen wir es überhaupt?** Eine Klasse kann viele Pferde erzeugen. Python muss wissen: *Welches* dieser Pferde ist gemeint? Bei 10 Pferden muss die Methode wissen: „Ich arbeite für DIESES Pferd hier.“

**Im Konstruktor `__init__`:**
- `self.name = name` bedeutet: **Speichere** den übergebenen `name` auf DIESEM Pferd.
- Ohne `self` würde Python nicht wissen, wo die Variable hingehört – sie würde nur lokal existieren und nach dem Aufruf verschwinden.

**In Methoden:**
- `self.name` bedeutet: **Lese den Namen** von DIESEM Pferd.
- Ohne `self` könnte die Methode nicht auf die Attribute des Objekts zugreifen – sie würde nicht wissen, ob es Lucky, Spirit oder ein anderes Pferd ist.

**So funktioniert der Aufruf im Hintergrund:**
- `lucky.wiehern()` wird von Python zu `Pony.wiehern(lucky)` übersetzt.
- Das erste Argument ist immer das Objekt selbst – deshalb heißt der Parameter `self`."""
