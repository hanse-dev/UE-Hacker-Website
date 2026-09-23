"""### Debug Quest – Task 3

🐛 Bug #3 – Goal: The program should print Level plus 1: 16. What is wrong?

**Explanation:** CSV reads all values as **text**. Before calculating, `int()` has to turn the text `\"15\"` into the number 15 – otherwise you get a `TypeError`."""