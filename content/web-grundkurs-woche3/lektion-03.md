# Sprungmarken

Auf langen Seiten hilft ein Menü, das direkt zu einem Abschnitt springt. Dafür brauchst du zwei Dinge:

1. Das **Ziel** bekommt eine `id`:
   ```html
   <section id="termine">…</section>
   ```
2. Der **Link** zeigt mit `#` auf diese id:
   ```html
   <a href="#termine">Zu den Terminen</a>
   ```

Ganz unten auf langen Seiten steht oft ein Link **nach oben**: `<a href="#top">Nach oben</a>` – mit `id="top"` am Seitenanfang.

> 💡 Groß- und Kleinschreibung zählt: `#Termine` findet `id="termine"` **nicht**.
