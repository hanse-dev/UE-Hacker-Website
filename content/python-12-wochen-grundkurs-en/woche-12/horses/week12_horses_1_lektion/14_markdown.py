"""## 💾 Stage 6: Saving and loading

*Knowledge from Week 9: JSON and files*

A good game remembers the game state. An object like `Player` cannot be saved as JSON directly, so we first turn it into a **dictionary** with name, position, HP and inventory (as a list of dictionaries).

Loading works backwards: the dictionary becomes a `Player` object again, with new `Item` objects. If the file does not exist, a `try/except` catches the `FileNotFoundError`."""