from position import Position


class Character:
    def __init__(self, x, y):
        self.position = Position(x, y)
        self.direction = 0
        self.symbols = ['^', '>', 'v', '<']

    def get_symbol(self):
        return self.symbols[self.direction]
