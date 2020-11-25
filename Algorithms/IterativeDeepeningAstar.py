import math
import sys

from SearchProblem import Node, SearchProblem

import Utilities.Heuristic

class IterativeDeepeningAstar(SearchProblem.SearchProblemSolver):
    def solve(self):
        max_depth = min(SearchProblem.MAX_DEPTH, Utilities.Heuristic.heuristic_chebyshev(
            self.start_node.state, self.problem.target))
        self.problem.num_of_nodes += 1
        while True:
            t = self.search([self.start_node], max_depth)
            if isinstance(t, int):
                if t == sys.maxsize:
                    return None
                max_depth = t
            else:
                return t

    def search(self, current_path, f_limit):
        def calculate_node_price(node):
            return node.path_cost + Utilities.Heuristic.heuristic_chebyshev(
                node.state, self.problem.target)

        current_node = current_path[-1]
        new_f = calculate_node_price(current_node)
        if new_f > f_limit:
            return new_f

        if self.is_goal(current_node.position):
            return current_node

        minValue = sys.maxsize
        successors = self.expand(current_node)
        successors.sort(key=calculate_node_price)

        self.problem.num_of_nodes += 1
        for child in successors:
            if child not in current_path:
                current_path.append(child)
                solution = self.search(current_path, f_limit)
                if isinstance(solution, int):
                    if solution < minValue:
                        minValue = solution
                else:
                    return solution
                current_path.pop()
        return minValue
