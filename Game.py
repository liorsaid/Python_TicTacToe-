from Board import Board
from Player import Player
import random
class Game:

    def __init__(self, player1, player2):
        self.board = Board()
        self.players = [player1, player2]
        self.current_player = player1

    def switch_player(self):
        if self.current_player == self.players[0]:
            self.current_player = self.players[1]
        else:
            self.current_player = self.players[0]
    
    def ifSame(self, one, two):
        while True:
            if(one == two):
                two = int(input(f"{player2_name} Please choose a different number between 1-3"))
            else:
                return two
            
    def play(self):
        while True:
            print("Who will start the game with X?" )
            numPlayer1 = int(input(f"{player1_name} Please choose number between 1-3"))
            numPlayer2 = int(input(f"{player2_name} Please choose number between 1-3"))
            numPlayer2 = self.ifSame(numPlayer1, numPlayer2)
            print("The number cohsen is:")
            rand = random.randint(1,3)
            print(rand)
            if rand == numPlayer1:
                self.current_player = player1
                break
            elif rand == numPlayer2:
                self.current_player = player2
                break
        while True:
            self.board.print_board()
            print(f"Player {self.current_player.name}'s turn.")
            row = int(input("Enter row (0, 1, 2): "))
            col = int(input("Enter column (0, 1, 2): "))

            if self.board.make_move(row, col, self.current_player):
                if self.board.is_winner(self.current_player):
                    self.board.print_board()
                    print(f"Player {self.current_player.name} wins! :)")
                    break
                elif self.board.is_full():
                    self.board.print_board()
                    print("It's a tie!")
                    break

                self.switch_player() 
            else:
                print("Invalid move. Try again.")


if __name__ == "__main__":
    player1_name = input("Enter Player 1's name: ")
    player2_name = input("Enter Player 2's name: ")

    player1 = Player(player1_name, "X")
    player2 = Player(player2_name, "O")

    game = Game(player1, player2)
    game.play()