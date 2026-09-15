# Problem: Class names must start with capital letters
# and __add__ should return a new object
class DataPacket:
    def __init__(self, size):
        self.size = size

    def __add__(self, other):
        return DataPacket(self.size + other.size)

    def __str__(self):
        return f"{self.size} MB"

packet1 = DataPacket(1024)
packet2 = DataPacket(2048)
total = packet1 + packet2
print(f"Total size: {total}")