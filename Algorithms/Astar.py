import math

from Algorithms import UCS
from typing import Tuple

import Utilities.Heuristic


def find_astar_route(problem):
    def f(n): return n.path_cost + \
        Utilities.Heuristic.heuristic_chebyshev(n.state, problem.target)
    solver = UCS.UCS(problem, f)
    solution, cost = solver()
    return solution, cost
