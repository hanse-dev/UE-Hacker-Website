"""### Debug Quest – Task 4

🐛 Bug #4 – Goal: Access should only be granted if the security level is at least 5 AND an ID card is present. At level 3 with an ID card, Access denied! should therefore appear. What is wrong?

**Explanation:** Both conditions must hold, so `and` is needed. With `or` a single true condition (the ID card) is enough."""