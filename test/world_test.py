from unittest import TestCase
from Tile import Tile
from World import World

class WorldTest(TestCase):
    
    def test_getAdjacentPositions(self):
        """
        should do .. when ..
        """ 
        # Arrange 
        world = World()

        # Act
        result = world.getAdjacentPositions(2, 2)
        expected = [(2, 1), (3, 1), (1,2), (3, 2), (1,3),(2,3)]

        # Assert
        self.assertEqual(len(result), len(expected))
        self.assertListEqual(sorted(result), sorted(expected))
        #self.assertListEqual(self.possiblePositions == [(502, 501), (500, 501), (501, 500), (502, 500), (500, 502), (501, 502)])
        
    def test_inserTile_invalidPosition(self):
        """
        If passed an invalid position to insert a tile, it raises an exception
        """
        # Arrange
        world = World()
        tile = Tile([1,0,0,0,0,0])
        # Act & Assert
        self.assertRaises(Exception, world.insertTile, tile, 5,5)
        
    def test_init_possiblePlacments(self):
        """
        should do .. when ..
        """
        
        # Arrange
        world = World()
        grasTile = Tile([1,0,0,0,0,0]) 

        # Act
        result = world.getPossiblePlacements(grasTile)

        # Assert
        expected = [(502, 501), (500, 501), (501, 500), (502, 500), (500, 502), (501, 502)]
        self.assertEqual(len(result), len(expected))
        self.assertListEqual(sorted(result), sorted(expected))

    def test_calculateBonsTiles_perfectTile(self):
        """
        should do .. when ..
        """
        
        # Arrange
        grasTile = Tile([1,0,0,0,0,0]) 
        world = World()
        
        
        # Act
        positions = world.getAdjacentPositions(501, 501)
        for pos in positions:
            world.insertTileAt(grasTile, pos)

        # Assert
        self.assertEqual(world.remainingTiles, 45)
        