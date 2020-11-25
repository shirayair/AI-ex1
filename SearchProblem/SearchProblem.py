import Problem, Node

MAX_DEPTH = 20


class SearchProblem:
    """This class performs an iterative deepening
    DFS search on a given graph.
    """

    def __init__(self, problem: Problem.ProblemSearch):
        self.problem = problem
        self.start_node = Node.Node(problem.s_start, 0)

    def __call__(self):
        return self.solve()

    def solve(self):
        raise NotImplementedError()

    def is_goal(self, node: Node.Node):
        return self.problem.is_goal(node)

    def expand(self, node):
        return node.expand(self.problem)
