
"""
Requirements:
SETUP:
1. Show Map of specified width and height, default to 9x9.
2. Show Character center of the Map.
3. Place and show a treasure on the map in random position that is not next to or on the player.

TURN: 
4. Ask user to if the they want to turn A--rotate-left, D--Rotate-Right or W-Move-straight.
5. Rotate or move character Move character in specified direction 
6. Block moves that would go off the map. If blocked then turn 180 degrees.
7. if player and treasure collide then remove treasure and add a new one in a blank square.
"""
from game import Game

# Tests
assert Game() is not None
assert Game().board.width == 9
assert Game().board.height == 9
assert Game().character.position.x == 4
assert Game().character.position.y == 4
assert Game().treasure.position.x != 4
assert Game().treasure.position.y != 4
assert Game().treasure.position.x >= 0
assert Game().treasure.position.x <= 8
assert Game().treasure.position.y >= 0
assert Game().treasure.position.y <= 8
assert Game().treasure.position.x != 4
assert Game().treasure.position.y != 4
assert Game().character.direction == 0


g = Game()
g.character.turn_right()
assert g.character.direction == 1
g.character.turn_right()
g.character.turn_right()
g.character.turn_right()
assert g.character.direction == 0
g.draw()