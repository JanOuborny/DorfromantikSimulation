from tile import Tile, EdgeType
from quest import Quest, QuestType
from typing import List, Set, Tuple

class World:
    MAX_SIZE = 1001
    CENTER = (500,500)

    def __init__(self) -> None:
        # Y down notation
        self.map: List[List[Tile]] = [[None for j in range(World.MAX_SIZE)] for i in range(World.MAX_SIZE)]
        self.possiblePlacements: Set[(int, int)] = [] # Keeps track of the possible placement positions
        self.quests: Set[Quest] = []

        # Place first tile
        self.map[World.CENTER[1]][World.CENTER[0]] = Tile([EdgeType.Gras, EdgeType.Gras, EdgeType.Gras, EdgeType.Gras, EdgeType.Gras, EdgeType.Gras])
        self.possiblePlacements = set(self.getAdjacentPositionsAt(World.CENTER))

    def insertTileAt(self, tile, pos: Tuple[int, int]) -> Tuple[int, int]:
        """
        Inserts tile. 
        Returns a tuple containing in the first entry the bonus tiles and in the second entry the score. 
        Throws exception if insertion is not possible.
        """
        x = pos[0]
        y = pos[1]

        if self.map[y][x] is not None:
            raise Exception(f"Invalid tile position at {pos}")
        
        adjacentTiles = self.getAdjacentTilesAt(pos)
        adjacentPositions = self.getAdjacentPositionsAt(pos)
        if len(adjacentTiles) > 0:
            self.map[y][x] = tile
            self.possiblePlacements.remove((x,y))

            for adjPos in adjacentPositions:
                if self.map[adjPos[1]][adjPos[0]] is None:
                    self.possiblePlacements.add(adjPos)

            score = self.calculateScoreAt(tile, pos)
            bonusTiles = self.calculateBonusTilesAt(pos)
            return (bonusTiles, score)
        else:
            raise Exception(f"Invalid tile position at {pos}")
        
    def getPossiblePlacements(self, tile) -> List[Tuple[int, int]]:
        # TODO filter tiles which doesnt match, i.e. river and train tiles
        return list(self.possiblePlacements)

    def getAdjacentTilesAt(self, pos: Tuple[int, int]) -> List[Tile]:
        """
        Returns the adjacent tiles in the hexagonal grid. In clockwise order, starting with Up-Right. 
        Empty positions are filled with None.
        """
        adjacentPositions = self.getAdjacentPositionsAt(pos)
        return [self.map[position[1]][position[0]] for position in adjacentPositions]

    def getAdjacentPositionsAt(self, pos: Tuple[int, int]) -> List[Tuple[int, int]]:
        """
        Returns the adjacent positios in the hexagonal grid. In clockwise order, starting with Up-Right
        """
        x = pos[0]
        y = pos[1]
        result = []
        result.append((x+1, y-1)) # Up Right
        result.append((x+1, y)) # Right
        result.append((x, y+1)) # Down Right
        result.append((x-1, y+1)) # Down Left
        result.append((x-1, y)) # Left
        result.append((x, y-1)) # Up Left
        return result
    
    def calculateScoreAt(self, tile, pos: Tuple[int, int]) -> int:
        """
        Calculates the score with the adjacent tiles of the provided position and the given tile.
        Note that the given tile doesn't need to correspond with the actual tile at the provided position.
        """
        score = 0
        adjacentPosition = self.getAdjacentPositionsAt(pos)
        for i in range(6):
            adjacentTile = self.getTileAt(adjacentPosition[i])
            if adjacentTile is not None:
                if tile.edges[i] == adjacentTile.edges[(i+3) % 6]:
                    score += 10
        return score

    def calculateBonusTilesAt(self, pos: Tuple[int, int]) -> int:
        """
        Checks if every adjacent tile of the provided position (and the tile at this position) is perfectly surrounded by tiles, i.e. every edge has matching type.
        """
        count = 0
        positionsToCheck = self.getAdjacentPositionsAt(pos)
        positionsToCheck.append(pos) # Check the tile at the provided position itself
        for pos in positionsToCheck:
            tileToCheck = self.getTileAt(pos)  
            if tileToCheck is not None:
                adjacentTiles = self.getAdjacentTilesAt(pos)
                if all(tile is not None for tile in adjacentTiles): # Otherwise cannot be perfect
                    score = self.calculateScoreAt(tileToCheck, pos)
                    if score == 60:
                        count += 1

        assert count <= 7
        return count         

    def getTileAt(self, pos):
        return self.map[pos[1]][pos[0]]
    