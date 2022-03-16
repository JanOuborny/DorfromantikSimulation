from typing import Set, Tuple
from tile import EdgeType

class Area:

    def __init__(self, type: EdgeType, size: int) -> None:
        self.size: int = size  
        self.type = type
        self.tiles: Set[Tuple[int, int]] = []
