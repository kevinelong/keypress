from board import Board
from character import Character
from treasure import Treasure
from position import Position


class Game:
    def __init__(self, width=9, height=9):
        self.board = Board(width, height)
        self.character = Character()
        self.board.place_center(self.character)
        self.board.place_random(Treasure())
        self.commands = {
            "left": self.turn_left,
            "right": self.turn_right,
            "forward": self.forward,
            "backward": self.backward,
        }

    def execute(self, command):
        if command in self.commands:
            self.commands[command]()
        else:
            print("unknown command: " + command)

    def get_map(self):
        return self.board.get_state()

    def turn_right(self):
        self.character.direction = (self.character.direction + 1) % 4
        self.board.redraw(self.character)

    def turn_left(self):
        self.character.direction = (self.character.direction - 1) % 4
        self.board.redraw(self.character)

    def apply_position(self, p):
        if self.board.is_on_board(p):
            self.board.move(self.character, p)

    def forward(self):
        self.apply_position([
                                lambda c: Position(c.position.x, c.position.y - 1),
                                lambda c: Position(c.position.x + 1, c.position.y),
                                lambda c: Position(c.position.x, c.position.y + 1),
                                lambda c: Position(c.position.x - 1, c.position.y),
                            ][self.character.direction](self.character))

    def backward(self):
        self.apply_position([
                                lambda c: Position(c.position.x, c.position.y + 1),
                                lambda c: Position(c.position.x - 1, c.position.y),
                                lambda c: Position(c.position.x, c.position.y - 1),
                                lambda c: Position(c.position.x + 1, c.position.y),
                            ][self.character.direction](self.character))

    def check_collisions(self):
        for item in self.board._content:
            if item != self.character and \
                    item.position.x == self.character.position.x and \
                    item.position.y == self.character.position.y:
                self.character.score += item.value
                self.board.place_random(Treasure())
                self.board.remove(item)
                break
