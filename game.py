from settings import *

class Game():
    def __init__(self, player_one, player_two):
        self.p1 = player_one
        self.p2 = player_two
        
    def update_board(self, game_board, visual_board):
        for i in range(len(game_board)):
            if len(game_board[i]) > 0 and len(game_board[i]) <= 6:
                for j in range(len(game_board[i])):
                    visual_board[i][j] = game_board[i][j]
        return visual_board
    
    def show_board(self, board):
        print("=============================")
        print("| {} | {} | {} | {} | {} | {} | {} |".format(board[0][5],board[1][5],board[2][5],board[3][5],board[4][5],board[5][5],board[6][5]))
        print("=============================")
        print("| {} | {} | {} | {} | {} | {} | {} |".format(board[0][4],board[1][4],board[2][4],board[3][4],board[4][4],board[5][4],board[6][4]))
        print("=============================")
        print("| {} | {} | {} | {} | {} | {} | {} |".format(board[0][3],board[1][3],board[2][3],board[3][3],board[4][3],board[5][3],board[6][3]))
        print("=============================")
        print("| {} | {} | {} | {} | {} | {} | {} |".format(board[0][2],board[1][2],board[2][2],board[3][2],board[4][2],board[5][2],board[6][2]))
        print("=============================")
        print("| {} | {} | {} | {} | {} | {} | {} |".format(board[0][1],board[1][1],board[2][1],board[3][1],board[4][1],board[5][1],board[6][1]))
        print("=============================")
        print("| {} | {} | {} | {} | {} | {} | {} |".format(board[0][0],board[1][0],board[2][0],board[3][0],board[4][0],board[5][0],board[6][0]))
        print("=============================")
    
    def column_is_full(self, game_board, chosen_column):
        if len(game_board[chosen_column]) == 6:
            return True
        else:
            return False
    
    def has_winner(self, visual_board):
        sample_1 = ["X","X","X","X"]
        sample_2 = ["O","O","O","O"]
        array = np.array(visual_board)
        flipped_array = np.fliplr(array)
        has_winner = False
        for i in range(1):
            # check columns for possible winner
            for i in range(7):
                if list(array[i, 0:4]) == sample_1 or list(array[i, 1:5]) == sample_1 or list(array[i, 2:]) == sample_1:
                    has_winner = True
                elif list(array[i, 0:4]) == sample_2 or list(array[i, 1:5]) == sample_2 or list(array[i, 2:]) == sample_2:
                    has_winner = True
            # check rows for possible winner
            flipped_visual_board = []
            for cell in range(6):
                row = []
                for col in visual_board:
                    row.append(col[cell])
                flipped_visual_board.append(row)
            for row in flipped_visual_board:
                if row[0:4] == sample_1 or row[1:5] == sample_1 or row[2:6] == sample_1 or row[3:] == sample_1 or \
                    row[0:4] == sample_2 or row[1:5] == sample_2 or row[2:6] == sample_2 or row[3:] == sample_2:
                    has_winner = True
            # check diagonals for possible winner
            if list(np.diag(array))[0:4] == sample_1 or list(np.diag(array))[1:5] == sample_1 or list(np.diag(array))[2:] == sample_1 or \
               list(np.diag(array, k=1))[0:4] == sample_1 or list(np.diag(array, k=1))[1:5] == sample_1 or list(np.diag(array, k=2)) == sample_1 or \
               list(np.diag(array, k=-1))[0:4] == sample_1 or list(np.diag(array, k=-1))[1:5] == sample_1  or list(np.diag(array, k=-1))[2:] == sample_1 or \
               list(np.diag(array, k=-2))[0:4] == sample_1 or list(np.diag(array, k=-2))[1:5] == sample_1 or list(np.diag(array, k=-3)) == sample_1 or \
               list(np.diag(flipped_array))[0:4] == sample_1 or list(np.diag(flipped_array))[1:5] == sample_1 or list(np.diag(flipped_array))[2:] == sample_1 or \
               list(np.diag(flipped_array, k=1))[0:4] == sample_1 or list(np.diag(flipped_array, k=1))[1:5] == sample_1 or list(np.diag(flipped_array, k=2)) == sample_1 or \
               list(np.diag(flipped_array, k=-1))[0:4] == sample_1 or list(np.diag(flipped_array, k=-1))[1:5] == sample_1  or list(np.diag(flipped_array, k=-1))[2:] == sample_1 or \
               list(np.diag(flipped_array, k=-2))[0:4] == sample_1 or list(np.diag(flipped_array, k=-2))[1:5] == sample_1 or list(np.diag(flipped_array, k=-3)) == sample_1:
                   has_winner = True
            elif list(np.diag(array))[0:4] == sample_2 or list(np.diag(array))[1:5] == sample_2 or list(np.diag(array))[2:] == sample_2 or \
                 list(np.diag(array, k=1))[0:4] == sample_2 or list(np.diag(array, k=1))[1:5] == sample_2 or list(np.diag(array, k=2)) == sample_2 or \
                 list(np.diag(array, k=-1))[0:4] == sample_2 or list(np.diag(array, k=-1))[1:5] == sample_2  or list(np.diag(array, k=-1))[2:] == sample_2 or \
                 list(np.diag(array, k=-2))[0:4] == sample_2 or list(np.diag(array, k=-2))[1:5] == sample_2 or list(np.diag(array, k=-3)) == sample_2 or \
                 list(np.diag(flipped_array))[0:4] == sample_2 or list(np.diag(flipped_array))[1:5] == sample_2 or list(np.diag(flipped_array))[2:] == sample_2 or \
                 list(np.diag(flipped_array, k=1))[0:4] == sample_2 or list(np.diag(flipped_array, k=1))[1:5] == sample_2 or list(np.diag(flipped_array, k=2)) == sample_2 or \
                 list(np.diag(flipped_array, k=-1))[0:4] == sample_2 or list(np.diag(flipped_array, k=-1))[1:5] == sample_2  or list(np.diag(flipped_array, k=-1))[2:] == sample_2 or \
                 list(np.diag(flipped_array, k=-2))[0:4] == sample_2 or list(np.diag(flipped_array, k=-2))[1:5] == sample_2 or list(np.diag(flipped_array, k=-3)) == sample_2:
                    has_winner = True
        return has_winner
    def board_is_full(self, board):
        columns_full = 0
        for col in board:
            if len(col) == 6:
                columns_full += 1
        if columns_full == 7:
            return True
        else:
            return False
        
    def run(self):
        turn = 1
        running = True
        while running:
            self.update_board(game_board, visual_board)
            self.show_board(visual_board)
            if self.has_winner(visual_board):
                if turn == 1:
                    print("The winner is player 2!")
                elif turn == -1:
                    print("The winner is player 1!")
                running = False
                break
            else:
                if self.board_is_full(game_board):
                    print("Board is full, but there's no winner!")
                    running = False
                    break
                                
            if turn == 1:
                pick_column = True
                while pick_column:
                    column = self.p1.choose_column()
                    if self.column_is_full(game_board, column):
                        print("Column full, choose another column.")
                        continue
                    else:
                        game_board[column].append(self.p1.symbol)
                        turn *= -1
                        pick_column = False
            elif turn == -1:
                pick_column = True
                while pick_column:
                    column = self.p2.choose_column()
                    if self.column_is_full(game_board, column):
                        print("Column full, choose another column.")
                        continue
                    else:
                        game_board[column].append(self.p2.symbol)
                        turn *= -1
                        pick_column = False