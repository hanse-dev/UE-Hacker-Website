"""### Debug Quest – Task 2

🐛 Bug #2 – Goal: The program should print Blitz. What is wrong?

**Explanation:** Without `self.` `name` and `level` are only local variables and disappear after `__init__`. With `self.name = name` they belong to the object."""