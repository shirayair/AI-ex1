import math

import UCS
from typing import Tuple

import Utilities


def find_astar_route(problem):
    def f(n): return UCS.g(n) + \
        Utilities.heuristic_chebyshev(n.state, problem.target)
    solution, cost = UCS.best_first_search(problem, f)
    return solution, cost
