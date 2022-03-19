from renderer import Renderer
from game import Game
from world import WorldException
import re


game = Game(11)
renderer = Renderer(game.world)

renderer.render('world.svg', addLabels=True, coordinateLabels=True)

while True:
    print("Enter the position to insert tile at:")
    try:
        inputPos = input()
        coords = [int(str) for str in re.findall(r'\d+', inputPos)]
        pos = (coords[0], coords[1])
        game.placeCurrentTileAt(pos)
        renderer.render('world.svg', addLabels=True, coordinateLabels=True)
        print(f"Tile inserted at {pos}")
    except WorldException as e:
        print(e)
