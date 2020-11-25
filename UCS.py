import math

import PriorityQueue
import PriorityQueue as pq
import Node


# in ucs we prioritize according to the cost up until the current node
def g(n):
    return n.path_cost


def find_ucs_route(problem):
    solution, cost = best_first_search(problem, g)
    return solution, cost


def best_first_search(problem, f):
    open_list = PriorityQueue.PriorityQueue(f)  # Priority Queue
    open_list.append(Node.Node(problem.source, 0))
    closed = set()
    while open_list:
        node = open_list.pop()
        if problem.is_goal(node.state):
            return node.solution()
        problem.num_of_nodes += 1
        closed.add(node.state)
        for child in node.expand(problem):
            if child.state not in closed and child not in open_list:
                open_list.append(child)
            elif child in open_list and f(child) < open_list[child]:
                print(f(child))
                print(open_list[child])
                del open_list[child]
                open_list.append(child)
    return None, None
