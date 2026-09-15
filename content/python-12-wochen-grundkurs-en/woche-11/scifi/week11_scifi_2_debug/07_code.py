class data_packet:
    def __init__(size):
        self.size = size

    def __add__(other):
        return self.size + other.size

packet1 = data_packet(1024)
packet2 = data_packet(2048)
total = packet1 + packet2
print(f"Total size: {total} MB")