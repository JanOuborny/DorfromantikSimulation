from enum import Enum
from typing import List
from random import randint
from quest import Quest
from area import Area

class EdgeType(Enum):
    Gras = 0
    Forest = 1
    Cornfield = 2
    Houses = 3
    Water = 4
    Train = 5
    WaterTrain = 6 # Omit first

class TileConnection:

    def __init__(self, area: Area) -> None:
        self.area = area

class Tile:

    def __init__(self, edges: List[EdgeType] = None, quest: Quest = None) -> None:    
        if edges is not None:
            assert len(edges) == 6
            self.edges = edges # Clockwise, starting with Up-Right
        else:
            self.edges: List[EdgeType] = []
            self.randomizeEdges()
        
        self.quest = quest
        self.connections: List[TileConnection] = [None for i in range(6)]  # Clockwise, starting with Up-Right
   
        for i in range(6):
            if self.edges[i] != EdgeType.Gras and self.connections[i] is not None:
                area = self.edges[i], randint(1, 2) # TODO vary size range by edge type
                self.connections[i] = TileConnection(area) 

                # All adjacent edges with the same type should have the same connection 
                if self.edges[i] == self.edges[i+1]: 
                    self.connections[i+1] = self.connections[i]

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
