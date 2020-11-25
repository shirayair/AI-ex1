import math

import UCS
from typing import Tuple


def heuristic_chebyshev(node: Tuple[int, int], goal: Tuple[int, int]) -> int:
    HEURISTIC_COEFFICIENT = 1

    xDiff = abs(node[0] - goal[0])
    yDiff = abs(node[1] - goal[1])
    return HEURISTIC_COEFFICIENT * (xDiff + yDiff) -\
        2 * HEURISTIC_COEFFICIENT * min(xDiff, yDiff)


def find_astar_route(problem):
    def f(n): return UCS.g(n) + heuristic_chebyshev(n.state, problem.target)
    solution, cost = UCS.best_first_search(problem, f)
    return solution, cost
