from typing import Tuple


def heuristic_chebyshev(node: Tuple[int, int], goal: Tuple[int, int]) -> int:
    HEURISTIC_COEFFICIENT = 1

    xDiff = abs(node[0] - goal[0])
    yDiff = abs(node[1] - goal[1])
    return HEURISTIC_COEFFICIENT * (xDiff + yDiff) -\
        2 * HEURISTIC_COEFFICIENT * min(xDiff, yDiff)
