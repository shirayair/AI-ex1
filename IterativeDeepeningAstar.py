import math
import sys

from node import Node

MAX_DEPTH = math.inf


def find_idastar_route(problem):
    global MAX_DEPTH
    start_node = Node(problem.source, 0)
    MAX_DEPTH = heuristic_chebyshev(start_node, problem.target)
    problem.num_of_nodes += 1
    while MAX_DEPTH < 20:
        f_limit = MAX_DEPTH
        MAX_DEPTH = math.inf
        node = search(problem, start_node, f_limit)
        if node:
            return node
    return None, None


def search(problem, start_node, f_limit):
    new_f = start_node.path_cost + \
        heuristic_chebyshev(start_node, problem.target)
    if new_f > f_limit:
        return None, new_f
    if problem.is_goal(start_node.state):
        return start_node.solution(), f_limit
    for child in start_node.expand(problem):
        solution = search(problem, child, f_limit)
        problem.num_of_nodes += 1
        if solution:
            return solution
    return None


def heuristic_chebyshev(node, goal):
    x1, y1 = node.state
    x2, y2 = goal
    dx = abs(x1 - x2)
    dy = abs(y1 - y2)
    return 1 * (dx + dy) + (-2) * min(dx, dy)
