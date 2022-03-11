from Tile import Tile
from typing import List

class World:
    MAX_SIZE = 1001
    MID_POINT = 500

    def __init__(self) -> None:
        self.map: List[List[Tile]] = [[None for j in range(World.MAX_SIZE)] for i in range(World.MAX_SIZE)]



    def insertTileAt(self, tile, x, y) -> int:
        """
        Inserts tile and returns score. 
        Returns -1 if insertion is not possible.
        """

        pass

    def getPossiblePositions(self, tile):
        pass

    def getAdjacentTiles(self, x, y):
        pass
    