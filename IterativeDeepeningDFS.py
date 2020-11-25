import SearchProblem

import Problem
import Node


class IterativeDeepeningDFS(SearchProblem.SearchProblem):
    """This class performs an iterative deepening
    DFS search on a given graph.
    """

    def solve(self):
        for max_depth in range(1, 20):
            res = self._dfs_search(max_depth)
            if res:
                return res

        return None, None

    def _dfs_search(self, max_depth: int):
        open_ls = [self.start_node]
        while open_ls:
            n = open_ls.pop()
            self.problem.num_of_nodes += 1
            if self.problem.is_goal(n):
                return n
            if n.depth < max_depth:
                open_ls.extend(n.expand(self.problem))
