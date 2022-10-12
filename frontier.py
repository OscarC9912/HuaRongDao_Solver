from board import BoardState
from typing import heapq

class Frontier2:

    def __init__(self, init: BoardState) -> None:
        self.contain = [init]

    def push(self, item: BoardState) -> None:
        heapq.heappush(self.contain, item)

    def select_min(self) -> BoardState:
        return [heapq.heappop(self.contain) for _ in range(1)]
