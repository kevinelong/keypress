from position import Position


class Treasure:
    def __init__(self, x, y):
        self.position = Position(x, y)

    def get_symbol(self):
        return "x"
