from unittest import TestCase
from typing import List
import random

from world import World
from tile import Tile, EdgeType
from renderer import Renderer

class MockWorldSmall(World):
    MAX_SIZE = 1

    def __init__(self):
        self.size = MockWorldSmall.MAX_SIZE
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
        self.size = MockWorldBig.MAX_SIZE
        self.map = [[Tile() if random.random() < 0.6 else None for i in range(MockWorldBig.MAX_SIZE)] for j in range(MockWorldBig.MAX_SIZE)]

class MockWorldFitting(World):
    MAX_SIZE = 2

    def __init__(self):
        # A [Tile] with houses for the [indices] and grass elsewhere.
        T = lambda indices: Tile(edges=[
            EdgeType.Houses if i in indices else EdgeType.Gras for i in range(6)
        ])

        self.size = MockWorldFitting.MAX_SIZE
        self.map = [
            [T([1, 2]), T([4])],
            [T([5]), T([])]
        ]

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

    def test_renderLabels(self):
        """
        should render a small svg with labels indicating the coordinates and
        edge indices.
        """

        # Arrange
        world = MockWorldSmall()
        renderer = Renderer(world)
        # Act
        renderer.render('test/render_labels.svg', addLabels=True)

    def test_renderBig(self):
        """
        should render the .svg even for big maps.
        """

        # Arrange
        world = MockWorldBig()
        renderer = Renderer(world)
        # Act
        renderer.render('test/render_big.svg')

    def test_renderFitting(self):
        """
        should render a connected spot of houses, ranging over three 3 tiles.
        """

        # Arrange
        world = MockWorldFitting()
        renderer = Renderer(world)
        # Act
        renderer.render('test/render_fitting.svg')
