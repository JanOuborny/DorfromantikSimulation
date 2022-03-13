from unittest import TestCase
from game import Game

class GameTest(TestCase):

    def test_placeCurrentTile_gameOver(self):
        """
        Should return true when the game is over
        """
        # Arrange
        game = Game()
        game.remainingTiles = 1
        # Act
        positions = game.getPossiblePlacements()
        pos = positions[0]
        gameOver = game.placeCurrentTile(pos[0],pos[1])
        # Assert
        self.assertTrue(gameOver)

    def test_placeCurrentTile_gameNotOver(self):
        """
        Should return false when the game is not over
        """
        # Arrange
        game = Game()
        game.remainingTiles = 2
        # Act
        positions = game.getPossiblePlacements()
        pos = positions[0]
        gameOver = game.placeCurrentTile(pos[0],pos[1])
        # Assert
        self.assertFalse(gameOver)