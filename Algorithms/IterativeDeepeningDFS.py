from SearchProblem import SearchProblem
from SearchProblem import Problem, Node


class IterativeDeepeningDFS(SearchProblem.SearchProblemSolver):
    """This class performs an iterative deepening
    DFS search on a given graph.
    """

    def solve(self):
        for max_depth in range(1, 20):
            self.problem.num_of_nodes += 1
            res = self._dfs_search(self.start_node, max_depth)
            if res:
                return res

        return None

    def _dfs_search(self, start_node: Node.Node, max_depth: int):
        if self.problem.is_goal(start_node.state):
            return start_node
        if start_node.depth >= max_depth:
            return

        for child in self.expand(start_node):
            self.problem.num_of_nodes += 1
            result = self._dfs_search(child, max_depth)
            if result:
                return result
