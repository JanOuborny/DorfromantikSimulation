from enum import Enum
from typing import Set, Tuple

# To prevent a circular import
class EdgeType:
    pass
class Area:
    pass

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
        self.area: Area = None
