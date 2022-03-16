from typing import Set, Tuple

# To prevent a circular import
class EdgeType:
    pass

class Area:

    def __init__(self, type: EdgeType, size: int) -> None:
        self.size: int = size  
        self.type = type
        self.tiles: Set[Tuple[int, int]] = []
