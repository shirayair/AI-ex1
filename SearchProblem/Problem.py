import itertools
import functools


class ProblemSearch:
    MOVE = {
        "R": (0, 1),
        "L": (0, -1),
        "U": (-1, 0),
        "D": (1, 0)
    }

    @staticmethod
    def points_add(*points):
        return functools.reduce(lambda x, y: (x[0]+y[0], x[1]+y[1]), points)

    @staticmethod
    def resolve_move(move_action: str):
        return ProblemSearch.points_add(*[ProblemSearch.MOVE[char] for char in move_action])

    @staticmethod
    def move(position, move_action):
        return ProblemSearch.points_add(position,
                                        ProblemSearch.resolve_move(move_action))

    def __init__(self, source, target, size, board):
        self.source = source
        self.size = size
        self.board = board
        self.target = target
        self.num_of_nodes = 0

    @staticmethod
    def get_all_possible_moves():
        actions = list("LURD")
        actions.extend([''.join(action)
                        for action in itertools.product(list("LR"), list("UD"))])
        return actions

    def validate_move(self, position, move_action):
        new_position = ProblemSearch.move(position, move_action)
        return new_position[0] >= 0 and new_position[0] < self.size \
            and new_position[1] >= 0 and new_position[1] < self.size

    def actions(self, position):
        return filter(lambda move_action: self.validate_move(position, move_action),
                      ProblemSearch.get_all_possible_moves())

    def succ(self, position, move_action):
        self.validate_move(position, move_action)
        return self.move(position, move_action)

    def is_goal(self, s):
        return s.position == self.target

    def step_cost(self, s):
        return self.board[s[0]][s[1]]

    def state_str(self, s):
        return '\n'.join([str(s[i * self.size:(i + 1) * self.size]) for i in range(0, self.size)])
