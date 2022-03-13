from typing import Tuple
from xmlrpc.client import boolean
from tile import Tile
from world import World
from typing import List, Tuple

class Game:

    def __init__(self) -> None:
        self.world = World()

        self.remainingTiles: int = 40
        self.score: int = 0
        self.currentTile = Tile()
    
    def getCurrentTile(self):
        return self.currentTile

    def getPossiblePlacements(self) -> List[Tuple[int, int]]:
        return self.world.getPossiblePlacements(self.currentTile)

    def getAdjacentTilesAt(self, pos) -> List[Tile]:
        """
        Returns the adjacent tiles in the hexagonal grid. In clockwise order, starting with Up-Right
        """
        return self.world.getAdjacentTilesAt(pos)

    def placeCurrentTileAt(self, pos) -> bool:
        """
        Places the current tile at the provided position.
        Returns a boolean indicating if the game is over.
        """
        result = self.world.insertTileAt(self.currentTile, pos)
        self.remainingTiles += (result[0] - 1)
        self.score += result[1]
        self.currentTile = Tile()

        return self.remainingTiles == 0