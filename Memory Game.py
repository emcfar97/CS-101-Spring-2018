#################################################################################
##
## CS 101
## Program #7
## Ethan McFarland
## Em463@mail.umkc.edu
##
## PROBLEM: Create a memory game that runs through turns until each cell has been
##          uncovered
##
## ALGORITHM: 
##      
## 
## ERROR HANDLING:
##      None
##
## OTHER COMMENTS:
##      None
##
#################################################################################

import string
import random

class Cell(object):

    def __init__(self, value):
        """
        :param value: The value that is currently in the cell.
        Initializes the cell with the value and sets it to not visible.
        :return:
        """
        self.value = value
        self.visible = False
    
    def __eq__(self, compare):
        """
        :param compare: Returns True if both instances have the same value.  False if not
        :return:
        """
        if str(self) == str(compare):
            return True
        return False

    def __str__(self):
        """
        :return: Returns the String representation of the cell.
                * if it is not visible.
                The value if it is visible.
        """
        if self.visible == True:
            return self.value
        return "*"

    def flip(self):
        """
        Flips over the cell.  Shows it, it if it was hidden.  Hides it, if it was shown.
        :return: None
        """
        self.visible = not self.visible


class Board(object):

    def __init__(self, size, board = [], values = []):
        """
        :param size: Sets up the instance given the size.
                size 1 : 3 x 4
                size 2 : 4 x 5
                size 3 : 4 x 6

        :return:
        Exceptions  : Raises a Value Error if the size is not 1, 2 or 3
                    raise ValueError("size must be 1, 2 or 3")
        """

        self.board = board
        
        size_list = {1:[3,4], 2:[4,5], 3:[4,6]}

        board_dimensions = size_list[size][0] * size_list[size][1] // 2
        
        while len(values) < board_dimensions:
            choice = string.ascii_uppercase[random.randint(0,25)]
            if choice not in values:
                values.append(choice)
                    
        for num, row in enumerate(range(size_list[size][0])):
            board.append([])
            for col in range(size_list[size][1]):
                value = values[random.randint(0,len(values)-1)]
                check = [col.value for row in board for col in row]
                while check.count(value) >= 2:
                    value = values[random.randint(0,len(values)-1)]
                    if check.count(value) < 2:
                        break
                board[num].append(Cell(value))        

    def __str__(self):
        """
        :return: String representation of the state of the board.
        """
        top_row = [i+1 for i in range(len(self.board[0]))]
        print('Memory Board\n'
              '{:>13}'.format(''), *top_row)
        for num, row in enumerate(self.board):
            print('{:>12}|'.format(num+1), *row)
        return str()
    
    def validate_choice(self, row, col):
        """
        :param row: the row being validated
        :param col: the column being validated
        :return: : None
        Exceptions.  Throws a ValueError if the row or column is not in the legals values
                    Also throws a ValueError if the cell is already being shown.
        """
        if row >= len(self.board):
            raise ValueError('Error : Row must be less than or equal to {}'.format(len(self.board)))
        elif col >= len(self.board[0]):
            raise ValueError('Error : Col must be less than or equal to {}'.format(len(self.board[0])))
        elif self.board[row][col].visible == True:
            raise KeyError('Error : {},{} cell is already being shown'.format(row+1,col+1))

    def play_choice1(self, row, col):
        """
        If the row, column is valid then it uncovers that row and column.
        :param row: int
        :param col: int
        :return: None
        """
        self.board[row][col].flip()
    
    def play_choice2(self, row, col):
        """
        If the row, column is valid then it uncovers that row and column.
        :param row: int
        :param col: int
        :return: None
        """
        self.board[row][col].flip()
    
    def end_turn(self, row_1, col_1, row_2, col_2):
        """ If the cells were not a match, then it flips the user choices back over.
        :return: None
        """
        if self.board[row_1][col_1] != self.board[row_2][col_2]:
            self.board[row_1][col_1].flip()
            self.board[row_2][col_2].flip()
            
    
    def game_over(self):
        """
        :return: bool - True if all the cells are uncovered, False if not.
        """
        cnt = length = 0
        for num1, row in enumerate(self.board):
            for num2, col in enumerate(row):
                length += 1
                if self.board[num1][num2].visible == True:
                    cnt += 1            
        if cnt == length:
            return True
        return False


if __name__ == "__main__":
    
    while True:
        #Retrieve and validate user input then populate board
        difficulty = input('How difficult should the game be? (1, 2, 3) ==>  ')
        try:
            difficulty = int(difficulty)
            if not (1 <= difficulty <= 3):
                raise ValueError
            board = Board(difficulty)
        except ValueError:
            print('You must enter an integer from 1 to 3')
            continue

        #Uncover first and second cells then check if board.game_over is True
        while True:
            while True:
                print(board)
                row_col1 = input('Enter the first row, col to uncover. Separated by commas ==>  ')
                try:
                    row_col1 = row_col1.split(',')
                    row_1 = int(row_col1[0]) - 1
                    col_1 = int(row_col1[1]) - 1
                    board.validate_choice(row_1, col_1)
                    board.play_choice1(row_1, col_1)
                    break
                except ValueError:
                    if type(row_1) != int:
                        print('The row must be an integer. Please try again')
                        continue
                    elif type(col_1) != int:
                        print('The col must be an integer. Please try again')
                        continue
                    elif type(row_1) and type(col_1) != int:
                        print('The row and col must be integers. Please try again\n')
                        continue
                except KeyError as error:
                    print(error)
                    continue
                
            while True:
                print(board)        
                row_col2 = input('Enter the second row, col to uncover. Separated by commas ==>  ')
                try:
                    row_col2 = row_col2.split(',')
                    row_2 = int(row_col2[0]) - 1
                    col_2 = int(row_col2[1]) - 1
                    board.validate_choice(row_2, col_2)
                    board.play_choice1(row_2, col_2)
                    break
                except ValueError:
                    if type(row_1) != int:
                        print('The row must be an integer. Please try again')
                        continue
                    elif type(col_1) != int:
                        print('The col must be an integer. Please try again')
                        continue
                    elif type(row_1) and type(col_1) != int:
                        print('The row and col must be integers. Please try again\n')
                        continue
                except KeyError as error:
                    print(error)
                    continue

            if board.game_over() == False:
                print(board)
                board.end_turn(row_1, col_1, row_2, col_2)
                continue
            else:
                break
        
        play = input('\nDo you want to play again? Y/YES/N/NO').upper()
        while not (play in ('Y', 'YES', 'N', 'NO')):
            play = input('You must enter Y YES N or NO\n\nDo you want to try another word? Y/YES/N/NO ==> ').upper()
        if play in ('Y', 'YES'):
            continue
        else:
            break
