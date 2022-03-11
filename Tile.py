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
    def __init__(self, edges: List[EdgeType]) -> None:    
        if edges is not None:
            self.edges = edges # Clockwise 
        else:
            self.edges: List[EdgeType] = []
            self.randomizeEdges()

    def randomizeEdges(self):
        enumOrder = len(list(EdgeType))
        for i in range(6):
            self.edges.append(randint(enumOrder))

    
    def rotate(self, n):
        """
        Rotates edge types clockwise by n
        """
        newEdges = []
        for i in range(6):
            newEdges.append(self.edges[i - (-n % 6)])
            
        self.edges = newEdges
