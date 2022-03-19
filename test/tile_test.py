from unittest import TestCase
from tile import Tile, EdgeType

class TileTest(TestCase):
    
    def test_rotate(self):
        # Arrange
        tile = Tile([1, 2, 3, 4, 5, 6])

        # Act
        tile.rotate(3)

        # Assert
        self.assertEqual(tile.edges[3], 1)


    def test_init_tileConnection(self):
        # Arrange & Act
        tile = Tile([EdgeType.Cornfield, EdgeType.Cornfield, EdgeType.Cornfield, EdgeType.Forest, EdgeType.Forest, EdgeType.Forest])

        # Assert
        for i in range(2):
            if i < 1:
                self.assertEquals(tile.connections[i], tile.connections[i+1])
            self.assertEqual(tile.connections[i].area.size, 3)

        for i in range(3,5):
            if i < 4:
                self.assertEquals(tile.connections[i], tile.connections[i+1])
            self.assertEqual(tile.connections[i].area.size, 3)
