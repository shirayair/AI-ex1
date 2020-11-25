import math
import sys

from SearchProblem import Node, SearchProblem

import Utilities.Heuristic


class IterativeDeepeningAstar(SearchProblem.SearchProblem):
    def solve(self):
        max_depth = Utilities.Heuristic.heuristic_chebyshev(
            self.start_node, self.problem.target)
        self.problem.num_of_nodes += 1
        while max_depth < SearchProblem.MAX_DEPTH:
            f_limit = max_depth
            max_depth = math.inf
            node = self.search(self.start_node, f_limit)
            if node:
                return node
        return None, None

    def search(self, current_node, f_limit):
        new_f = current_node.path_cost + \
            Utilities.Heuristic.heuristic_chebyshev(
                current_node, self.problem.target)
        if new_f > f_limit:
            return None, new_f
        if self.is_goal(current_node.position):
            return current_node.solution(), f_limit
        for child in self.expand(current_node):
            solution = self.search(child, f_limit)
            self.problem.num_of_nodes += 1
            if solution:
                return solution
        return None
