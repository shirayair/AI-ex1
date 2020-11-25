import math

from Algorithms import UCS
from typing import Tuple

import Utilities.Heuristic
import math

from Utilities import PriorityQueue

from SearchProblem import SearchProblem
from SearchProblem import Node, Problem


class AStar(SearchProblem.SearchProblemSolver):
    def __call__(self):
        return self.solve()

    def solve(self):
        def f(n): return n.path_cost + \
            Utilities.Heuristic.heuristic_chebyshev(
                n.position, self.problem.target)
        solver = UCS.UCS(self.problem, f)
        return solver()
