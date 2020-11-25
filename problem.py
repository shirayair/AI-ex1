class ProblemSearch:

    def __init__(self, source, target, size, board):
        self.source = source
        self.size = size
        self.board = board
        self.target = target
        self.num_of_nodes = 0

    def actions(self, s):
        moves = []
        x, y = s[0], s[1]
        if y < self.size - 1 and self.board[x][y + 1] != -1:
            moves.append('R')
            if x < self.size - 1 and self.board[x + 1][y] != -1 and self.board[x + 1][y + 1] != -1:
                moves.append('RD')
            if x > 0 and self.board[x - 1][y] != -1 and self.board[x - 1][y + 1] != -1:
                moves.append('RU')
        if x < self.size - 1 and self.board[x + 1][y] != -1:
            moves.append('D')
        if y > 0 and self.board[x][y - 1] != -1:
            moves.append('L')
            if x < self.size - 1 and self.board[
                    x + 1][y] != -1 and self.board[x + 1][y - 1] != -1:
                moves.append('LD')
            if x > 0 and self.board[x - 1][y] != -1 and self.board[x - 1][y - 1] != -1:
                moves.append('LU')
        if x > 0 and self.board[x - 1][y] != -1:
            moves.append('U')
        return moves

    def succ(self, s, action):
        if action == 'R':
            return s[0], s[1] + 1
        if action == 'RD':
            return s[0] + 1, s[1] + 1
        if action == 'D':
            return s[0] + 1, s[1]
        if action == 'LD':
            return s[0] + 1, s[1] - 1
        if action == 'L':
            return s[0], s[1] - 1
        if action == 'LU':
            return s[0] - 1, s[1] - 1
        if action == 'U':
            return s[0] - 1, s[1]
        if action == 'RU':
            return s[0] - 1, s[1] + 1

    def is_goal(self, s):
        return s == self.target

    def step_cost(self, s):
        return self.board[s[0]][s[1]]

    def state_str(self, s):
        return '\n'.join([str(s[i * self.size:(i + 1) * self.size]) for i in range(0, self.size)])


if __name__ == '__main__':
    print("hi")
