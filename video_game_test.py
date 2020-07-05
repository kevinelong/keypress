"""
Requirements:
SETUP:
1. Show Map of specified width and height, default to 9x9.
2. Show Character center of the Map.
3. Place and show a treasure on the map in random position that is not on the player's position.

TURN: 
4. Ask user to if the they want to turn A--rotate-left, D--Rotate-Right or W-Move-straight.
5. Rotate or move character Move character in specified direction 
6. Block moves that would go off the map.
7. if player and treasure collide then add treasure's value to player score.
7. if player and treasure collide then remove treasure from map.
7. if player and treasure collide then add a new treasure in a blank square.
"""
from game import Game

# Tests
assert Game() is not None
assert Game().board._width == 9
assert Game().board._height == 9
assert Game().character.position.x == 4
assert Game().character.position.y == 4
assert Game().character.direction == 0

g = Game()
g.turn_right()
assert g.character.direction == 1
g.turn_right()
g.turn_right()
g.turn_right()
assert g.character.direction == 0

map = [
    ['.', '.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '^', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.', '.']
]

result = g.get_map()
# print(result)
assert len(map) == len(result)
assert len(map[0]) == len(result[0])
