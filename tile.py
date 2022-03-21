from ast import Break
from enum import Enum
from typing import List
from random import randint
from quest import Quest
from area import Area
import queue

class EdgeType(Enum):
    Gras = 0
    Forest = 1
    Cornfield = 2
    Houses = 3
    Water = 4
    Train = 5
    WaterTrain = 6 # Omit first

class TileConnection:
    """
    Represents the interior connection of edges with the same type
    """
    def __init__(self, area: Area) -> None:
        self.area = area

class Tile:
    """
    Represents a tile in the game world
    """
    def __init__(self, edges: List[EdgeType] = None, quest: Quest = None) -> None:    
        if edges is not None:
            assert len(edges) == 6
            self.edges = edges # Clockwise, starting with Up-Right
        else:
            self.edges: List[EdgeType] = []
            self.randomizeEdges()

        self.connections: List[TileConnection] = [None for i in range(6)]  # Clockwise, starting with Up-Right
        self._initTileConnections()

        self.quest = quest
        # TODO Assert that the edges of the quest's type are all connected

    def randomizeEdges(self):
        enumOrder = len(list(EdgeType))
        for i in range(6):
            self.edges.append(EdgeType(randint(0, enumOrder - 1)))

        return self

    def getIndexOfOppositeSide(index: int):
        """
        Returns the index of the opposite side of an given edge index
        """
        return (index+3) % 6

    def rotate(self, n):
        """
        Rotates edge types clockwise by n
        """
        newEdges = []
        for i in range(6):
            newEdges.append(self.edges[i - (-n % 6)])

        self.edges = newEdges

    def _initTileConnections(self):
        # Expand TileConnection of first tile by going counterclockwise around
        j = 1
        self.connections[0] = TileConnection(Area(self.edges[0], 1))
        while self.connections[-j] is None:
            if self.edges[0] == self.edges[-j]:
                self.connections[0].area.size += 1
                self.connections[-j] = self.connections[0]
                j = (j + 1) % 6 
            else:
                break
    
        # Expand TileConnection of remaining tiles by going clockwise around.
        q = queue.Queue()
        q.put(0)
        while not q.empty():
            i = q.get()

            if self.connections[i] is None:
                area = Area(self.edges[i], 1) # TODO Implement area size
                self.connections[i] = TileConnection(area)

            j = (i + 1) % 6
            while self.connections[j] is None:
                if self.edges[i] == self.edges[j]:
                    self.connections[i].area.size += 1
                    self.connections[j] = self.connections[i] 
                else:
                    q.put(j)
                    break
                j = (j + 1) % 6
