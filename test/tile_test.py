from unittest import TestCase
from tile import Tile

class TileTest(TestCase):
    
    def test_rotate(self):
        # Arrange
        tile = Tile([1, 2, 3, 4, 5, 6])

        # Act
        tile.rotate(3)

        # Assert
        self.assertEqual(tile.edges[3], 1)