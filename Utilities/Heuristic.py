from typing import Tuple


def heuristic_chebyshev(node: Tuple[int, int], goal: Tuple[int, int]) -> int:
    xDiff = abs(node[0] - goal[0])
    yDiff = abs(node[1] - goal[1])
    return max(xDiff, yDiff)
