"""### Debug Quest – Task 3

🐛 Bug #3 – Goal: The program should print Age plus 1: 9. What is wrong?

**Explanation:** CSV reads all values as **text**. Before calculating, `int()` has to turn the text `\"8\"` into the number 8 – otherwise you get a `TypeError`."""