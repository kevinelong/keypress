import random
from position import Position


class Board:
    def __init__(self, width=9, height=9):
        self.width = width
        self.height = height
        self.content = []

    def add_item(self, item):
        self.content.append(item)

    def place_center(self, item):
        item.position = Position(self.width // 2, self.height // 2)
        self.content.append(item)

    def random_position(self):
        return Position(random.randint(0, self.width), random.randint(0, self.height))

    def place_random(self, item):
        p = self.random_position()
        tries = 0
        while self.is_occupied(p) and tries < 999:
            p = self.random_position()
            tries += 1
        item.position = p
        self.content.append(item)

    def is_occupied(self, position):
        if position is None:
            return False
        for item in self.content:
            if item.position is not None:
                if item.position.x == position.x and item.position.y == position.y:
                    return True
        return False

    def get_state(self):
        output = []
        for y in range(0, self.height):
            line = []
            for x in range(0, self.width):
                symbol = "."
                for item in self.content:
                    if item.position.x == x and item.position.y == y:
                        symbol = item.get_symbol()
                        break
                line.append(symbol)
            output.append(line)
        return output

    def is_on_board(self, position):
        if position.x < 0:
            return False
        elif position.y < 0:
            return False
        elif position.x + 1 > self.width:
            return False
        elif position.y + 1 > self.height:
            return False
        return True
