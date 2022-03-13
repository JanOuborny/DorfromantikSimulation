from tile import Tile, EdgeType
from typing import List, Set, Tuple

class World:
    MAX_SIZE = 1001
    CENTER = (500,500)

    def __init__(self) -> None:
        # Y down notation
        self.map: List[List[Tile]] = [[None for j in range(World.MAX_SIZE)] for i in range(World.MAX_SIZE)]
        self.possiblePlacements: Set[(int, int)] = [] # Keeps track of the possible placement positions

        # Place first tile
        self.map[World.CENTER[1]][World.CENTER[0]] = Tile([EdgeType.Gras, EdgeType.Gras, EdgeType.Gras, EdgeType.Gras, EdgeType.Gras, EdgeType.Gras])
        self.possiblePlacements = set(self.getAdjacentPositions(World.CENTER[0], World.CENTER[1]))

    def insertTileAt(self, tile, pos: Tuple[int, int]) -> int:
        self.insertTile(tile, pos[0], pos[1])

    def insertTile(self, tile, x, y) -> Tuple[int, int]:
        """
        Inserts tile. 
        Returns a tuple containing in the first entry the bonus tiles and in the second entry the score. 
        Throws exception if insertion is not possible.
        """
        if self.map[y][x] is not None:
            raise Exception(f"Invalid tile position at {(x,y)}")
        
        adjacentTiles = self.getAdjacentTiles(x, y)
        adjacentPositions = self.getAdjacentPositions(x, y)
        if len(adjacentTiles) > 0:
            self.map[y][x] = tile
            self.possiblePlacements.remove((x,y))

            for pos in adjacentPositions:
                if self.map[y][x] is None:
                    self.possiblePlacements.add(pos)

            score = self.calculateScore(tile, x, y)
            bonusTiles = self.calculateBonusTiles(tile, x, y)
            return (bonusTiles, score)
        else:
            raise Exception(f"Invalid tile position at {(x,y)}")
        
    def getPossiblePlacements(self, tile) -> List[Tuple[int, int]]:
        # TODO filter tiles which doesnt match, i.e. river and train tiles
        return list(self.possiblePlacements)

    def getAdjacentTiles(self, x, y) -> List[Tile]:
        adjacentPositions = self.getAdjacentPositions(x, y)
        result = []

        for pos in adjacentPositions:
            if self.map[pos[1]][pos[0]] is not None:
                result.append(self.map[pos[1]][pos[0]])
        
        return result

    def getAdjacentPositions(self, x, y) -> List[Tuple[int, int]]:
        """
        Returns the adjacent positios in the hexagonal grid. In clockwise order, starting with Up-Right
        """
        result = []
        result.append((x+1, y-1)) # Up Right
        result.append((x+1, y)) # Right
        result.append((x, y+1)) # Down Right
        result.append((x-1, y+1)) # Down Left
        result.append((x-1, y)) # Left
        result.append((x, y-1)) # Up Left
        return result
    
    def calculateScore(self, tile, x, y) -> int:
        score = 0
        adjacentPosition = self.getAdjacentPositions(x, y)
        for i in range(6):
            adjacentTile = self.getTileAt(adjacentPosition[i])
            if adjacentTile is not None:
                if tile.edges[i] == adjacentTile.edges[(i+3) % 6]:
                    score += 10
        return score

    def calculateBonusTiles(self, tile, x, y) -> int:
        """
        Checks if every adjacent tile of the provided tile is perfectly surrounded by tiles, i.e. every edge has matching type.
        """
        count = 0
        positionsToCheck = self.getAdjacentPositions(x, y)
        positionsToCheck.append((500, 500)) # Check the placed tile itself
        for pos in positionsToCheck:
            tileToCheck = self.getTileAt(pos)  
            if tileToCheck is not None:
                adjacentTiles = self.getAdjacentTiles(pos[0], pos[1])
                if len(adjacentTiles) == 6: # Otherwise cannot be perfect
                    score = self.calculateScore(tileToCheck, pos[0], pos[1])
                    if score == 60:
                        count += 1

        assert count <= 6
        return count
                


    def getTileAt(self, pos):
        return self.map[pos[1]][pos[0]]
    