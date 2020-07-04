class Board:
    def __init__(self, width=9, height=9):
        self.width = width
        self.height = height
        self.content = []

    def add_item(self, item):
        self.content.append(item)

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
