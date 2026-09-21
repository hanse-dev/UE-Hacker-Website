"""### Debug Quest – Task 3

🐛 Bug #3 – Goal: The program should print Rank plus 1: 5. What is wrong?

**Explanation:** CSV reads all values as **text**. Before calculating, `int()` has to turn the text `\"4\"` into the number 4 – otherwise you get a `TypeError`."""