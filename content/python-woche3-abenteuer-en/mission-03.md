# ⭐⭐⭐⭐☆ Mission 3: The Champions Arena

In the arena, fighters are rated by their performance. A fighter has a **level**, a number of **wins** and a number of **losses**. The **win rate** is `wins / (wins + losses)`.

| Rating | Rule |
|--------|------|
| LEGENDARY | level >= 50 **and** win rate > 0.8 |
| MASTER | level >= 30 **and** win rate > 0.6 |
| perfect streak bonus | losses == 0 (checked separately with its own `if`) |

**Bonus (optional, not checked):** Also take the total number of fights into account!
