import operator
import functools

from SearchProblem.Problem import ProblemSearch


class Node:
    MOVE = {
        "R": (0, 1),
        "L": (0, -1),
        "U": (-1, 0),
        "D": (1, 0)
    }

    @staticmethod
    def resolve_move(move_code: str):
        result = []
        for char in move_code:
            result.append(Node.MOVE[char])
        return tuple(functools.reduce(lambda x, y: [x[0]+y[0], x[1]+y[1]], result))

    @staticmethod
    def __validate_action(move_code: str):
        if move_code is None:
            return

        assert 1 <= len(move_code) <= 2
        for char in move_code:
            assert char in Node.MOVE
        assert Node.resolve_move(move_code) != [0, 0]

    @property
    def state(self):
        return self.position

    def __init__(self, position,
                 parent=None,
                 action: str = None,
                 path_cost: int = 0):
        self.__validate_action(action)
        assert path_cost >= 0

        self.position = position
        self.parent = parent
        self.action = action
        self.path_cost = path_cost
        self.depth = 0
        if parent:
            self.depth = parent.depth + 1

    def expand(self, problem):
        return [self.child_node(problem, action)
                for action in problem.actions(self.position)]

    def child_node(self, problem, action):
        next_position = problem.succ(self.position, action)
        next_node = Node(next_position, self, action,
                         self.path_cost + problem.step_cost(next_position))
        return next_node

    def solution(self):
        return '-'.join([node.action for node in self.path()[1:]]), self.path_cost

    def path(self):
        node, path_back = self, []
        while node:
            path_back.append(node)
            node = node.parent
        return list(reversed(path_back))

    def __repr__(self):
        return f"<{self.position}>"

    def __lt__(self, node):
        if node.depth == self.depth:
            return ProblemSearch.ORDERED_MOVED.index(self.action) < \
                ProblemSearch.ORDERED_MOVED.index(node.action)
        return self.depth > node.depth

    def __eq__(self, other):
        return isinstance(other, Node) and self.position == other.position

    def __ne__(self, other):
        return not (self == other)
