from settings import *
from players import *
from game import *

player = Player("X")
computer = Computer()
game = Game(player, computer)


game_board[1].append("X")
game_board[1].append("X")
game_board[1].append("X")
game_board[1].append("O")
game_board[1].append("X")


sample_1 = ["X","X","X","X"]
sample_2 = ["O","O","O","O"]

has_winner = False
no_winner = True
while no_winner:
    for col in game_board:
        if (col[0:4] or col[1:5] or col[2:]) == sample_1:
            has_winner = True
    else:
        no_winner = False
            
print(has_winner)
