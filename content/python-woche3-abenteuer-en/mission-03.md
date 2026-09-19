# ⭐⭐⭐⭐☆ Mission 3: The Champion's Arena

In the arena, fighters are rated by their performance! From wins and losses you calculate the **win rate** (`wins / (wins + losses)`) and check it together with the level – with `and`.

| Rating | Rule |
|--------|------|
| LEGENDARY | level >= 50 **and** win rate > 0.8 |
| MASTER | level >= 30 **and** win rate > 0.6 |
| FIGHTER | everyone else |
| perfect streak bonus | losses == 0 (checked separately with its own `if`) |

**Bonus (optional, not checked):** Also take the total number of fights into account!
