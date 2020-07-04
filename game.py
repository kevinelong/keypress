from board import Board
from character import Character
from treasure import Treasure
from position import Position


class Game:
    def __init__(self, width=9, height=9):
        self.board = Board(width, height)
        self.character = Character(width // 2, height // 2)
        self.treasure = Treasure(2, 2)
        self.board.add_item(self.treasure)
        self.board.add_item(self.character)

    def draw(self):
        self.board.draw()

    def turn_right(self):
        self.character.direction = (self.character.direction + 1) % 4

    def turn_left(self):
        self.character.direction = (self.character.direction - 1) % 4

    def forward(self):
        c = self.character
        p = Position(c.position.x, c.position.y)
        if c.direction == 0:
            p.y -= 1
        elif c.direction == 1:
            p.x += 1
        elif c.direction == 2:
            p.y += 1
        elif c.direction == 3:
            p.x -= 1

        if self.board.is_on_board(p):
            c.position = p

    def backward(self):
        c = self.character
        p = Position(c.position.x, c.position.y)
        if c.direction == 0:
            p.y += 1
        elif c.direction == 1:
            p.x -= 1
        elif c.direction == 2:
            p.y -= 1
        elif c.direction == 3:
            p.x += 1

        if self.board.is_on_board(p):
            c.position = p

    def check_collisions(self):
        for item in self.board.content:
            if item != self.character and item.position.x == self.character.position.x and item.position.y == self.character.position.y:
                self.board.content.remove(item)
                break
