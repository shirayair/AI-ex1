import math

from Algorithms import UCS
from typing import Tuple

import Utilities.Heuristic


def find_astar_route(problem):
    def f(n): return UCS.g(n) + \
        Utilities.Heuristic.heuristic_chebyshev(n.state, problem.target)
    solution, cost = UCS.best_first_search(problem, f)
    return solution, cost
