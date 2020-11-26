import itertools
import functools

from typing import Tuple


class ProblemSearch:
    ORDERED_MOVED = ["R", "RD", "D", "LD", "L", "LU", "U", "RU"]
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
        return ProblemSearch.ORDERED_MOVED

    def _is_diagonal_move(self, move_action):
        return len(move_action) == 2

    def _is_within_borders(self, position):
        return position[0] >= 0 and position[0] < self.size \
            and position[1] >= 0 and position[1] < self.size

    def _is_wall(self, position):
        return self.board[position[0]][position[1]] == -1

    def _validate_diagonal_no_wall(self, position, move_action):
        """Checks that a diagonal move is valid, this function assumes
        that the move is legal, i.e. does not step outside the board.

        Args:
            position (Tuple[int, int]): new position
            move_action (str): Diagonal action (two words)

        Returns:
            bool: 
        """
        firstMove, secondMove = move_action[0], move_action[1]
        return not any((self._is_wall(ProblemSearch.move(position, firstMove)),
                        self._is_wall(ProblemSearch.move(position, secondMove))))

    def validate_move(self, position, move_action):
        new_position = ProblemSearch.move(position, move_action)
        if not self._is_within_borders(new_position):
            return False

        if self._is_diagonal_move(move_action):
            if not self._validate_diagonal_no_wall(position, move_action):
                return False

        return not self._is_wall(new_position)

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
