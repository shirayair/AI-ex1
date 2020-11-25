import Problem
import Node


class IterativeDeepeningDFS:
    """This class performs an iterative deepening
    DFS search on a given graph.
    """
 
    def __init__(self, problem: Problem.ProblemSearch):
        self.problem = problem
        self.start_node = Node.Node(problem.s_start, 0)

    def __call__(self):
        return self.find_ids_route()

    def find_ids_route(self):
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
