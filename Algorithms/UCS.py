import math

from Utilities import PriorityQueue

from SearchProblem import SearchProblem
from SearchProblem import Node, Problem


def default_evaluator(node: Node.Node):
    return node.path_cost


class UCS(SearchProblem.SearchProblemSolver):
    def __init__(self, problem: Problem.ProblemSearch, evaluator=default_evaluator):
        self.evaluator = evaluator
        super(UCS, self).__init__(problem)

    def solve(self):
        open_list = PriorityQueue.PriorityQueue(
            self.evaluator)  # Priority Queue
        open_list.append(self.start_node)
        closed = set()
        while open_list:
            node = open_list.pop()
            if self.is_goal(node):
                return node.solution()
            self.problem.num_of_nodes += 1
            closed.add(node.position)
            for child in self.expand(node):
                if child.position not in closed and child not in open_list:
                    open_list.append(child)
                elif child in open_list and self.evaluator(child) < open_list[child]:
                    del open_list[child]
                    open_list.append(child)
        return None, None
