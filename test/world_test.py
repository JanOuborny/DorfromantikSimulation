from unittest import TestCase
from tile import EdgeType, Tile
from world import World, WorldException
from quest import Quest, QuestType

class WorldTest(TestCase):
    
    def test_getAdjacentPositionsAt(self):
        """
        Should return the correct coordinates for adjacent positions  
        """ 
        # Arrange 
        world = World()
        # Act
        result = world.getAdjacentPositionsAt((2, 2))
        expected = [(2, 1), (3, 1), (1,2), (3, 2), (1,3),(2,3)]
        # Assert
        self.assertEqual(len(result), len(expected))
        self.assertListEqual(sorted(result), sorted(expected))
        
    def test_inserTileAt_disconnectedPosition(self):
        """
        Should raise an exception if an invalid position is passed
        """
        # Arrange
        world = World(10)
        tile = Tile([1,0,0,0,0,0])
        # Act & Assert
        self.assertRaises(WorldException, world.insertTileAt, tile, (0,0))

    def test_insertTileAt_updateTileConnections(self):
        """
        should do .. when ..
        """     
        # Arrange
        world = World(10)
        tile = Tile([EdgeType.Gras,EdgeType.Gras,EdgeType.Gras,EdgeType.Gras,EdgeType.Gras,EdgeType.Gras])
        # Act
        world.insertTileAt(tile, world.getPossiblePlacements(tile)[0])
        # Assert
        center = world.getTileAt(world.center)
        for connection in tile.connections:
            for centerCon in center.connections:
                self.assertEquals(connection.area, centerCon.area)
        
    def test_insertTileAt_updateQuestArea(self):
        """
        Should update the quest area of the inserted tile
        """
        
        # Arrange
        world = World(10)
        tile = Tile([EdgeType.Gras,EdgeType.Gras,EdgeType.Gras,EdgeType.Gras,EdgeType.Gras,EdgeType.Gras])
        tile.quest = Quest(QuestType.Atleast, EdgeType.Gras, 100)
        # Act
        world.insertTileAt(tile, world.getPossiblePlacements(tile)[0])
        # Assert
        centerTile = world.getTileAt(world.center)
        self.assertEquals(centerTile.connections[0].area, tile.quest.area)

    def test_insertTileAt_questCompleted(self):
        """
        Should return the correct number of rewarded tiles and the completed quest is removed from the quest set
        """
        # Arrange
        world = World(10)
        tile = Tile([EdgeType.Gras,EdgeType.Gras,EdgeType.Gras,EdgeType.Gras,EdgeType.Gras,EdgeType.Gras])
        tile.quest = Quest(QuestType.Exact, EdgeType.Gras, 12)
        # Act
        result = world.insertTileAt(tile, world.getPossiblePlacements(tile)[0])
        # Assert
        self.assertEqual(result[0], 5)
        self.assertTrue(len(world.quests) == 0)
        
        
    def test_getPossiblePlacments_afterInit(self):
        """
        Should return the correct possible placements after init of World
        """
        # Arrange
        world = World()
        grasTile = Tile([1,0,0,0,0,0]) 
        # Act
        result = world.getPossiblePlacements(grasTile)
        # Assert
        expected = [(501, 500), (499, 500), (500, 499), (501, 499), (499, 501), (500, 501)]
        self.assertEqual(len(result), len(expected))
        self.assertListEqual(sorted(result), sorted(expected))

    def test_calculateBonusTilesAt_perfectTile(self):
        """
        Should return one bonus tile when enclosing a tile perfectly, i.e. matching edge types at each edge
        """
        # Arrange
        grasTile = Tile([EdgeType.Gras,EdgeType.Gras,EdgeType.Gras,EdgeType.Gras,EdgeType.Gras,EdgeType.Gras]) 
        world = World()
        # Act
        positions = world.getAdjacentPositionsAt(world.center)
        for pos in positions:
            world.insertTileAt(grasTile, pos)
        # Assert
        result = world.calculateBonusTilesAt(world.center)
        self.assertEqual(result, 1)

    def test_getAdjacentTilesAt_noAdjacentTiles(self):
        """
        Should return with six elements where each element is None
        """
        # Arrange
        world = World()
        # Act
        result = world.getAdjacentTilesAt(world.center)
        # Assert
        self.assertEqual(len(result), 6)
        self.assertTrue(all(tile is None for tile in result))
        
        