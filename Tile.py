from enum import Enum
from typing import List
from random import randint


class EdgeType(Enum):
    Gras = 0
    Forest = 1
    Cornfield = 2
    Houses = 3
    Water = 4
    Train = 5
    WaterTrain = 6 # Omit first

class Tile:

    def __init__(self, edges: List[EdgeType] = None) -> None:    
        if edges is not None:
            assert len(edges) == 6
            self.edges = edges # Clockwise, starting with Up-Right
        else:
            self.edges: List[EdgeType] = []
            self.randomizeEdges()

    def randomizeEdges(self):
        enumOrder = len(list(EdgeType))
        for i in range(6):
            self.edges.append(EdgeType(randint(0, enumOrder - 1)))

        return self


    def rotate(self, n):
        """
        Rotates edge types clockwise by n
        """
        newEdges = []
        for i in range(6):
            newEdges.append(self.edges[i - (-n % 6)])

        self.edges = newEdges
