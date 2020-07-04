from position import Position


class Character:
    def __init__(self):
        self.position = None
        self.direction = 0
        self.symbols = ['^', '>', 'v', '<']
        self.score = 0

    def get_symbol(self):
        return self.symbols[self.direction]
