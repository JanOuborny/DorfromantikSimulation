from unittest import TestCase

from world import World
from tile import Tile, EdgeType
from renderer import Renderer

class MockWorldSmall(World):
    MAX_SIZE = 1

    def __init__(self):
        self.map = [
            [
                Tile([
                    EdgeType.Gras,
                    EdgeType.Forest,
                    EdgeType.Cornfield,
                    EdgeType.Houses,
                    EdgeType.Water,
                    EdgeType.Train,
                ])
            ]
        ]

class MockWorldBig(World):
    MAX_SIZE = 50

    def __init__(self):
        self.map = [[Tile([]).randomizeEdges() for i in range(MockWorldBig.MAX_SIZE)] for j in range(MockWorldBig.MAX_SIZE)]

class TestRenderer(TestCase):
    def test_renderSmall(self):
        """
        should render the .svg file when called.
        """

        # Arrange
        world = MockWorldSmall()
        renderer = Renderer(world)

        # Act
        renderer.render('test/render_small.svg')

    def test_renderBig(self):
        """
        should render the .svg even for big maps.
        """

        # Arrange
        world = MockWorldBig()
        renderer = Renderer(world)
        # Act
        renderer.render('test/render_big.svg')
        # Assert
