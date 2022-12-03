from player import HumanPlayer, RandomComputerPlayer, GeniusComputerPlayer
import time 
class TicTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(9)]
        self.current_winner =None #keep track of current winner

    def print_board(self):
        for row in [self.board[(i*3):(i+1)*3] for i in range(3)]:
            print('|'+'|'.join(row)+'|')
    
    @staticmethod
    def print_board_nums():
        # tells us what number corresponds to what box 0|1|2 [[0,1,2], [3,4,5], [6,7,8]]
        number_board = [[str(i) for i in range(j*3,(j+1)*3)] for j in range(3)]
        for row in number_board:
            print('|'+'|'.join(row)+'|')

    def available_moves(self):
        #get the list of squares that are empty
        moves = []
        for (i,spot) in enumerate(self.board):
            # [ 'x','o','x'] -> [(0,'x'), (1,'o'), (2,'x')]
            if spot == ' ':
                moves.append(i)
        return moves
        #return [i for i,spot in enumerate(self.board) if spot == ' ']

    def make_move(self,square,letter): #filling in the board with X and O if the move is valid, else ask them to enter again
        if self.board[square] == ' ':
            self.board[square] = letter
            if self.winner(square,letter):
                self.current_winner = letter
            return True
        return False

    def empty_squares(self): #check for empty squares 
        return ' ' in self.board

    def num_empty_squares(self):
        return self.board.count(' ')

    def winner(self,square,letter): #finding if there is a winner along row, column or diagonals
        row_ind = square // 3
        row = self.board[ row_ind*3: (row_ind+1)*3]
        if all([spot==letter for spot in row]): #check for row
            return True
        
        col_ind = square % 3
        column = [self.board[col_ind+i*3] for i in range(3)]
        if all([spot == letter for spot in column]): #check for column
            return True

        # diagonal squares are even numbers [0,2,4,6,8]
        if square%2==0 :
            diagonal1 = [self.board[i] for i in [0,4,8]] # left to right diagonal
            diagonal2 = [self.board[i] for i in [2,4,6]] # right to left diagonal

            if all([spot==letter for spot in diagonal1]):
                return True
            if all([spot==letter for spot in diagonal2]):
                return True
        
        #if all these checks fail
        return False

def play(game, x_player, o_player, print_game=True): #print_game won't be needed for comp vs comp
    if print_game:
        game.print_board_nums()
    
    letter = 'X' # starting letter

    #iterate till the board has empty sqaures. When there is a winner that will be returned.
    while game.empty_squares():
        #get move from the appropriate player
        if letter == 'O':
            square = o_player.get_move(game)
        else:
            square = x_player.get_move(game)
        
        #let's make a move!
        if game.make_move(square,letter):
            if print_game:
                print(letter + f' makes a move to {square}')
                game.print_board()
                print('')
        
            if game.current_winner:
                if print_game:
                    print(letter + ' wins!')
                return letter
            #after we make move we need to alternate the player
            letter = 'O' if letter == 'X' else 'X'
            #tiny pause
            time.sleep(0.8)

    if print_game:
        print('It\'s a tie!')


if __name__ == '__main__':
    x_player = HumanPlayer('X')
    o_player = GeniusComputerPlayer('O')
    t = TicTacToe()
    play(t,x_player,o_player,print_game=True)