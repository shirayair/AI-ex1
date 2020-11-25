import math

import UCS


def find_astar_route(problem):
    def f(n): return UCS.g(n) + heuristic_chebyshev(n, problem.target)
    solution, cost = UCS.best_first_search(problem, f)
    return solution, cost


def uclid(x, y):
    return math.sqrt(pow(x.ix - y.ix, 2) + pow(x.iy - y.iy, 2))


def heuristic_chebyshev(node, goal):
    x1, y1 = node.state
    x2, y2 = goal
    dx = abs(x1 - x2)
    dy = abs(y1 - y2)
    return 1 * (dx + dy) + (-2) * min(dx, dy)


def max_ind_dif(x, y):
    return max(abs(x.ix - y.ix), abs(x.iy - y.ix))
