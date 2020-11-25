import itertools
import functools

from typing import Tuple


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
        return ["R", "RD", "D", "LD", "L", "LU", "U", "RU"]

    def validate_move(self, position, move_action):
        new_position = ProblemSearch.move(position, move_action)
        
        if new_position[0] >= 0 and new_position[0] < self.size \
            and new_position[1] >= 0 and new_position[1] < self.size:
            return self.board[new_position[0]][new_position[1]] != -1
        return False

    def actions(self, position):
        return filter(lambda move_action: self.validate_move(position, move_action),
                      ProblemSearch.get_all_possible_moves())

    def succ(self, position, move_action):
        self.validate_move(position, move_action)
        return self.move(position, move_action)

    def is_goal(self, s: Tuple[int, int]):
        return s == self.target

    def step_cost(self, s):
        return self.board[s[0]][s[1]]

    def state_str(self, s):
        return '\n'.join([str(s[i * self.size:(i + 1) * self.size]) for i in range(0, self.size)])
