"""## 🪞 Warum `self`? – Der Schlüssel zu deinen Objekten

**Was ist `self`?** `self` ist die Referenz auf **das konkrete Objekt**, das gerade angesprochen wird. Wenn du `enterprise.starten()` aufrufst, ist `self` in der Methode genau das Objekt `enterprise`.

**Warum brauchen wir es überhaupt?** Eine Klasse kann viele Objekte erzeugen. Python muss wissen: *Welches* dieser Objekte ist gemeint? Bei 10 Raumschiffen muss die Methode wissen: „Ich arbeite für DIESES Schiff hier.“

**Im Konstruktor `__init__`:**
- `self.name = name` bedeutet: **Speichere** den übergebenen `name` auf DIESEM Objekt.
- Ohne `self` würde Python nicht wissen, wo die Variable hingehört – sie würde nur lokal existieren und nach dem Aufruf verschwinden.

**In Methoden:**
- `self.name` bedeutet: **Lese den Namen** von DIESEM Objekt.
- Ohne `self` könnte die Methode nicht auf die Attribute des Objekts zugreifen – sie würde nicht wissen, ob es Enterprise, Millennium oder ein anderes Schiff ist.

**So funktioniert der Aufruf im Hintergrund:**
- `enterprise.starten()` wird von Python zu `Raumschiff.starten(enterprise)` übersetzt.
- Das erste Argument ist immer das Objekt selbst – deshalb heißt der Parameter `self`."""
