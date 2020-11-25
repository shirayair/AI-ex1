class Node:
    def __init__(self, state, parent=None, action=None, path_cost=0):
        self.state = state
        self.parent = parent
        self.action = action
        self.path_cost = path_cost
        self.depth = 0
        self.action_map = {
            'RU': 7,
            'U': 6,
            'LU': 5,
            'L': 4,
            'LD': 3,
            'D': 2,
            'RD': 1,
            'R': 0,
        }
        if parent:
            self.depth = parent.depth + 1

    def expand(self, problem):
        return [self.child_node(problem, action)
                for action in problem.actions(self.state)]

    def child_node(self, problem, action):
        next_state = problem.succ(self.state, action)
        next_node = Node(next_state, self, action,
                         self.path_cost + problem.step_cost(next_state))
        return next_node

    def solution(self):
        return [node.action for node in self.path()[1:]], self.path_cost

    def path(self):
        node, path_back = self, []
        while node:
            path_back.append(node)
            node = node.parent
        return list(reversed(path_back))

    def __repr__(self):
        return f"<{self.state}>"

    def __lt__(self, node):
        return self.action_map[self.action] < self.action_map[node.action]

    def __eq__(self, other):
        return isinstance(other, Node) and self.state == other.state

    def __ne__(self, other):
        return not (self == other)
