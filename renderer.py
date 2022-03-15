import svgwrite
from typing import List, Tuple

from world import World
from tile import EdgeType


class Point:
    """
    y-up coordinate in the svg image.
    """
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def asList(self) -> List[int]:
        return [self.x, self.y]

    def __str__(self):
        return f"{self.x}, {self.y}"

class Renderer:
    """
    Beware: We use Point(x, y) instead of (y, x) and y-up.
    The conversion happens in [render()].
    """

    _edgeTypeToColor = {
        EdgeType.Gras: 'lawngreen',
        EdgeType.Forest: 'green',
        EdgeType.Cornfield: 'khaki',
        EdgeType.Houses: 'lightgray',
        EdgeType.Water: 'aqua',
        EdgeType.Train: 'gray',
        EdgeType.WaterTrain: 'lightblue' # Omit first
    }

    _TRIANGLE_SIDE_LENGTH = 0.61803398875

    # Do not draw lines, just shapes.
    STYLE = (
        'stroke-width:0;'
    )

    def __init__(self, world: World):
        self.world = world

    def render(self, filename: str = 'render.svg'):
        assert filename.endswith('.svg'), "Suck my dickkkkkk"

        dwg = svgwrite.Drawing(
            filename=filename,
            profile='full',
            size=('30cm', '20cm'),
            viewBox=(f'{-0.5} {-0.5} {1.5 * self.world.MAX_SIZE + 1} {self.world.MAX_SIZE + 1}'),
            style=Renderer.STYLE
        )

        for y, row in enumerate(self.world.map):
            for x, tile in enumerate(row):
                # Add y/2 for shift in y-down coordinate system.
                center = Point(x + y / 2, y)

                for edgeIndex, edge in enumerate(tile.edges):
                    color = Renderer._edgeTypeToColor[edge]
                    Renderer._drawEdge(dwg, center, edgeIndex, color, label=f"({x}, {y})")

                # Renderer._addLabel(dwg, str((x, y)), center)

        dwg.save()

    # def _addLabel(dwg, text: str, center: Point):
    #     dwg.add(svgwrite.shapes.Circle(center=(center.x, center.y), r=0.2, style="fill:#FFFFFF88;"))
    #     dwg.add(dwg.text(text, insert=(center.x, center.y), font_size="0.1px",fill='black', text_anchor='middle', dominant_baseline='central'))


    def _drawEdge(dwg, center: Point, edgeIndex: int, color: str, label: str):
        """
        [color] should be given has hex code as name.
        """

        if edgeIndex == 0:
            Renderer._drawTriangle(dwg, center, Renderer._top(center), Renderer._topRight(center), color)
        elif edgeIndex == 1:
            Renderer._drawTriangle(dwg, center, Renderer._topRight(center), Renderer._bottomRight(center), color)
        elif edgeIndex == 2:
            Renderer._drawTriangle(dwg, center, Renderer._bottomRight(center), Renderer._bottom(center), color)
        elif edgeIndex == 3:
            Renderer._drawTriangle(dwg, center, Renderer._bottom(center), Renderer._bottomLeft(center), color)
        elif edgeIndex == 4:
            Renderer._drawTriangle(dwg, center, Renderer._bottomLeft(center), Renderer._topLeft(center), color)
        elif edgeIndex == 5:
            Renderer._drawTriangle(dwg, center, Renderer._topLeft(center), Renderer._top(center), color)
        else:
            raise Exception(f"edgeIndex out of bounds: {edgeIndex}")

    def _drawTriangle(dwg: svgwrite.Drawing, a: Point, b: Point, c: Point, color: str):
        dwg.add(svgwrite.shapes.Polygon(
            points=[a.asList(), b.asList(), c.asList()],
            style=f"fill:{color};"
        ))

    def _top(center: Point) -> Point:
        return Point(center.x, center.y + Renderer._TRIANGLE_SIDE_LENGTH)

    def _topRight(center: Point) -> Point:
        return Point(center.x + 0.5, center.y + Renderer._TRIANGLE_SIDE_LENGTH / 2)

    def _bottomRight(center: Point) -> Point:
        return Point(center.x + 0.5, center.y - Renderer._TRIANGLE_SIDE_LENGTH / 2)

    def _bottom(center: Point) -> Point:
        return Point(center.x, center.y - Renderer._TRIANGLE_SIDE_LENGTH)

    def _bottomLeft(center: Point) -> Point:
        return Point(center.x - 0.5, center.y - Renderer._TRIANGLE_SIDE_LENGTH / 2)

    def _topLeft(center: Point) -> Point:
        return Point(center.x - 0.5, center.y + Renderer._TRIANGLE_SIDE_LENGTH / 2)
