
from enum import Enum
from tile import EdgeType, Tile
from typing import Set, Tuple

class QuestType(Enum):
    Atleast = 0
    Exact = 1
    Closure = 2

class Quest:

    def __init__(self, questType: QuestType, edgeType: EdgeType, goal: int) -> None:
        self.type = questType
        self.edgeType = edgeType
        self.reward = 5
        self.goal = goal

        self._area: Set[Tuple[int, int]] = Set()
