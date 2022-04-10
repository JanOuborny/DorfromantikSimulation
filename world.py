import queue
from tile import Tile, EdgeType
from quest import Quest, QuestType
from typing import List, Set, Tuple

class WorldException(Exception):
    pass

class World:
    DEFAULT_SIZE = 1001

    def __init__(self, size: int = DEFAULT_SIZE) -> None:
        self.size = size
        self.center = (round((self.size-1) / 2), round((self.size-1) / 2))
        self.quests: Set[Quest] = set()

        # Y down notation
        self.map: List[List[Tile]] = [[None for j in range(self.size)] for i in range(self.size)]
        self.possiblePlacements: Set[(int, int)] = set() # Keeps track of the possible placement positions
        

        # Place first tile
        self.map[self.center[1]][self.center[0]] = Tile([EdgeType.Gras, EdgeType.Gras, EdgeType.Gras, EdgeType.Gras, EdgeType.Gras, EdgeType.Gras])
        self.possiblePlacements = set(self.getAdjacentPositionsAt(self.center))

    def insertTileAt(self, tile, pos: Tuple[int, int]) -> Tuple[int, int]:
        """
        Inserts tile. 
        Returns a tuple containing in the first entry the rewarded tiles and in the second entry the score. 
        Throws exception if insertion is not possible.
        """
        x = pos[0]
        y = pos[1]

        if self.map[y][x] is not None:
            raise WorldException(f"Invalid tile position at {pos}: Position is occupied.")
        if pos not in self.possiblePlacements: # This may become inefficent when the set of possible placements becomes very large
            raise WorldException(f"Invalid tile position at {pos}: Disconnected from remaining tiles.")
        
        self.map[y][x] = tile

        adjacentTiles = self.getAdjacentTilesAt(pos)
        adjacentPositions = self.getAdjacentPositionsAt(pos)

        # Check if the tile matches, i.e. water and train tiles are aligned.
        tileMatches = True
        if EdgeType.Train in tile.edges or EdgeType.Water in tile.edges:
            for i in range(6):
                if self.edges[i] == EdgeType.Train or self.edges[i] == EdgeType.Water:
                    if self.edges[i] != tile.edges[i]:
                        tileMatches = False
                        break 
        if not tileMatches:
            raise WorldException(f"Invalid tile position at {pos}: Water or train edges don't align.")
 
        # Update tile connections
        for adjTile in adjacentTiles:
            for i in range(6):
                if adjTile is not None:
                    # The same area can be be attached to multiple edges. However, we only count its sizes once.
                    if (tile.edges[i] == adjTile.edges[Tile.getIndexOfOppositeSide(i)] and 
                            tile.connections[i].area != adjTile.connections[Tile.getIndexOfOppositeSide(i)].area):
                        adjacentConnection = adjTile.connections[Tile.getIndexOfOppositeSide(i)]
                        adjacentConnection.area.size += tile.connections[i].area.size
                        tile.connections[i].area = adjacentConnection.area 

        # Set the quest area to the adjacent 
        if tile.quest is not None:
            index = next(i for i,e in enumerate(tile.edges) if e == tile.quest.edgeType)
            tile.quest.area = tile.connections[index].area
            self.quests.add(tile.quest)

        rewardedTiles = self._updateQuests()

        # Update possible placements
        self.possiblePlacements.remove((x,y))
        # Append new possible placements
        for adjPos in adjacentPositions:
            if self.map[adjPos[1]][adjPos[0]] is None:
                self.possiblePlacements.add(adjPos)

        score = self.calculateScoreAt(tile, pos)
        bonusTiles = self.calculateBonusTilesAt(pos)
        return (bonusTiles + rewardedTiles, score)
        
    def getPossiblePlacements(self, tile) -> List[Tuple[int, int]]:
        """
        Returns the positions on the map where a tile can be possiblz placed.
        This can include positions where the current tile cannot be placed, because the edge types don't match.
        """
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
                if tile.edges[i] == adjacentTile.edges[Tile.getIndexOfOppositeSide(i)]:
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
    
    def _updateQuests(self) -> int:
        """
        Checks for completed or failed quets and updates the open quest set.
        Returns the rewarded tiles for completed quests.
        """
        rewardedTiles = 0
        completedQuests = set()
        for quest in self.quests:
            if quest.type == QuestType.Atleast:
                if quest.area.size >= quest.goal:
                    rewardedTiles += quest.reward
                    completedQuests.add(quest)
            elif quest.type == QuestType.Exact:
                if quest.area.size == quest.goal:
                    rewardedTiles += quest.reward
                    completedQuests.add(quest)
                elif quest.area.size > quest.goal:
                    # Quest failed
                    completedQuests.add(quest)
        self.quests = self.quests.difference(completedQuests)
        return rewardedTiles