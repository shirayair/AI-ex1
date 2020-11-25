from node import Node


def find_ids_route(problem):
    for i in range(1, 20):
        # if there is a path, it will hold the last node in the path
        res = DFS_L(problem, Node(problem.s_start, 0), i)
        if res:
            return res
        return None, None


def DFS_L(problem, start_node, max_depth):
    # creating node from start state and adding to open
    open_ls = list()
    open_ls.append(start_node)
    while len(open_ls) > 0:
        n = open_ls.pop()
        problem.num_of_nodes += 1
        # can't compare nodes, need to compare state
        if problem.is_goal(n):
            return n
        if n.depth < max_depth:
            children = n.expand(problem)
            open_ls += children
    return None
