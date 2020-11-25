from SearchProblem import Problem
from SearchProblem import Node

MAX_DEPTH = 20


class SearchProblemSolver:
    """This class performs an iterative deepening
    DFS search on a given graph.
    """

    def __init__(self, problem: Problem.ProblemSearch):
        self.problem = problem
        self.start_node = Node.Node(problem.source, 0)

    def __call__(self):
        solution = self.solve()
        if solution is None:
            return None, None
        return solution.solution()

    def solve(self):
        raise NotImplementedError()

    def is_goal(self, node: Node.Node):
        return self.problem.is_goal(node)

    def expand(self, node):
        return node.expand(self.problem)
