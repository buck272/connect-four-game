from settings import *
from players import *
from game import *

player = Player("X")
computer = Computer()
game = Game(player, computer)


for col in game_board:
    for i in range(6):
        col.append("X")
        
print(game_board)

array = np.array(visual_board)
print(array[:,0:4])