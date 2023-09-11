import Player
class Board:
    def __init__(self):
        self.board = [[" " for _ in range(3)] for _ in range(3)]

    def print_board(self):
        for row in self.board:
            print(" | ".join(row))
            print("-" * 9)

    def is_full(self):
        return all(cell != " " for row in self.board for cell in row)

    def is_winner(self, player):
        for row in self.board:
            if all(cell == player.symbol for cell in row):
                return True
        for col in range(3):
            if all(self.board[row][col] == player.symbol for row in range(3)):
                return True
        if all(self.board[i][i] == player.symbol for i in range(3)) or all(self.board[i][2 - i] == player.symbol for i in range(3)):
            return True
        return False

    def make_move(self, row, col, player):
        if 0 <= row < 3 and 0 <= col < 3 and self.board[row][col] == " ":
            self.board[row][col] = player.symbol
            return True
        return False
