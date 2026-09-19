# ⭐⭐⭐⭐☆ Mission 3: The Mission Rating

The mission is rated based on its performance! Use these values:

| Level | Success points | Losses | Time |
|---|---|---|---|
| 9 | 90 | 1 | 24 |

The **score** is: `success_points - (losses * 10) - (time / 5)`

**Rating levels:**
- level >= 10 **and** score >= 85 **and** losses == 0 → `LEGENDARY!`
- level >= 8 **and** score >= 70 **and** losses <= 2 → `EXCELLENT!`
- otherwise → `Mission completed.`

**Speed bonus:** If time < 30, print `+50 Bonus for lightning mission!`

> 💡 **Tip:** You decide how to build it – there is no single right way!

**Bonus (optional, not checked):** Also take the mission difficulty into account!
