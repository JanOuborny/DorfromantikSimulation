from unittest import TestCase
from tile import EdgeType, Tile
from world import World

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
        
    def test_inserTileAt_invalidPosition(self):
        """
        Should raise an exception if an invalid position is passed
        """
        # Arrange
        world = World()
        tile = Tile([1,0,0,0,0,0])
        # Act & Assert
        self.assertRaises(Exception, world.insertTileAt, tile, (5,5))
        
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
        
        