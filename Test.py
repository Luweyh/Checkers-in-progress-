# Author: Luwey Hon
# This is what a push is
class Checkers:

    def __init__(self):
        self._board = [['_' for _ in range(8)] for _ in range(8)]
        self._game_state = 'UNFINISHED'

        odd_list = [1,3,5,7]
        even_list = [0,2,4,6]

        for num in even_list:
            self._board[6][num] = 'X'
            self._board[0][num] = 'O'
            self._board[2][num] = 'O'

        for num in odd_list:
            self._board[1][num] = 'O'
            self._board[5][num] = 'X'
            self._board[7][num] = 'X'

    def get_game_state(self):
        return self._game_state

    def check_piece(self, player, from_row, from_col):

        if self._game_state != 'UNFINISHED':
            return False

        if self._board[from_row][from_col] != player:
            print('Invalid location, try again')
            return False

        print('Allowed piece chosen')

        # verify normal piece
        if player == 'X' or player == 'O':
            return 'checker'

        # verify if king
        if player == 'xX' or player == 'oO':
            return 'king'

        return True

    def move_checker(self, player, from_row, from_col, to_row, to_col):
        """ Moves current player """

        if self._game_state != 'UNFINISHED':
            return False

        if 0 > to_row < 8 or 0 > to_col <8:
            return False

        if player == 'X':
            if from_row - 1 == to_row and (from_col - 1 == to_col or from_col + 1 == to_col):
                if self._board[to_row][to_col] == '_':
                    self._board[to_row][to_col] = player
                    self._board[from_row][from_col] = '_'
                    print('Move successful')
                    return True
                else:
                    print('Invalid move, try again')
                    return False

            elif from_row - 2 == to_row:

                self.x_eats(from_row, from_col, to_row, to_col)
                return True

            else:
                print('Invalid move, try again')
                return False


        elif player == 'O':
            if from_row + 1 == to_row and (from_col - 1 == to_col or from_col + 1 == to_col):
                if self._board[to_row][to_col] == '_':
                    self._board[to_row][to_col] = player
                    self._board[from_row][from_col] = '_'
                    print('Move successful')
                    return True
                else:
                    print('Invalid move, try again')
                    return False

            elif from_row + 2 == to_col:
                self.o_eats(from_row, from_col, to_row, to_col)
                return True

            else:
                print('Invalid move, try again')
                return False

    def x_eats(self, from_row, from_col, to_row, to_col):

        # x moves and eats O to diagonal left
        if self._board[from_row - 1][from_col -1] == 'O' and self._board[to_row][to_col] == '_' and from_row == to_row + 2 and from_col == to_col + 2:
            self._board[to_row][to_col] = 'X'
            self._board[from_row -1][from_col -1] = '_'
            self._board[from_row][from_col] = '_'
            self.print_board()

            # double eats
            from_row = to_row
            from_col = to_col

            while (self._board[from_row - 1][from_col - 1] == 'O' and self._board[to_row - 2][to_col - 2] == '_') or \
                    (self._board[from_row - 1][from_col + 1] == 'O' and self._board[to_row - 2][to_col + 2] == '_'):
                move_again = (input("You can eat again, would you like to move again? (y/n)"))
                if move_again == 'y':
                    row = int(input("which row would you like to move to?"))
                    col = int(input('which column would you like to move to?'))
                    player = 'X'
                    self.move_checker(player, from_row, from_col, row, col)
                    self.print_board()

                elif move_again == 'n':
                    break

                else:
                    print('Invalid answer, try again')

        # eats diagonal right
        elif self._board[from_row -1][from_col+1] == 'O' and self._board[to_row][to_col] == '_' and from_row == to_row + 2 and from_col == to_col -2:
            self._board[to_row][to_col] = 'X'
            self._board[from_row -1][from_col + 1] = '_'
            self._board[from_row][from_col] = '_'
            self.print_board()

            # for double eats.
            from_row = to_row
            from_col = to_col

            while (self._board[from_row - 1][from_col -1] == 'O' and self._board[to_row -2][to_col -2] == '_') or \
                    (self._board[from_row - 1][from_col +1] == 'O' and self._board[to_row-2][to_col +2] == '_'):
                move_again = (input("You can eat again, would you like to move again? (y/n)"))
                if move_again == 'y':
                    row = int(input("which row would you like to move to?"))
                    col = int(input('which column would you like to move to?'))
                    player = 'X'
                    self.move_checker(player, from_row, from_col, row, col)
                    self.print_board()

                elif move_again == 'n':
                    break

                else:
                    print('Invalid answer, try again')



        return True

    def o_eats(self, from_row, from_col, to_row, to_col):

        # o moves and eats X to diagonal left
        if self._board[from_row + 1][from_col - 1] == 'X' and self._board[to_row][to_col] == '_' and from_row == to_row - 2 and from_col == to_col + 2:
            self._board[to_row][to_col] = 'O'
            self._board[from_row + 1][from_col - 1] = '_'
            self._board[from_row][from_col] = '_'
            self.print_board()

            # double eats
            from_row = to_row
            from_col = to_col

            while (self._board[from_row + 1][from_col - 1] == 'X' and self._board[to_row + 2][to_col - 2] == '_') or \
                    (self._board[from_row + 1][from_col + 1] == 'O' and self._board[to_row + 2][to_col + 2] == '_'):
                move_again = (input("You can eat again, would you like to move again? (y/n)"))
                if move_again == 'y':
                    row = int(input("which row would you like to move to?"))
                    col = int(input('which column would you like to move to?'))
                    player = 'X'
                    self.move_checker(player, from_row, from_col, row, col)
                    self.print_board()

                elif move_again == 'n':
                    break

                else:
                    print('Invalid answer, try again')

        # eats diagonal right
        elif self._board[from_row + 1][from_col + 1] == 'X' and self._board[to_row][to_col] == '_' and from_row == to_row - 2 and from_col == to_col - 2:
            self._board[to_row][to_col] = 'O'
            self._board[from_row + 1][from_col + 1] = '_'
            self._board[from_row][from_col] = '_'

            # for double eats.
            from_row = to_row
            from_col = to_col

            while (self._board[from_row + 1][from_col - 1] == 'X' and self._board[to_row + 2][to_col - 2] == '_') or \
                    (self._board[from_row + 1][from_col + 1] == 'X' and self._board[to_row + 2][to_col + 2] == '_'):
                move_again = (input("You can eat again, would you like to move again? (y/n)"))
                if move_again == 'y':
                    row = int(input("which row would you like to move to?"))
                    col = int(input('which column would you like to move to?'))
                    player = 'X'
                    self.move_checker(player, from_row, from_col, row, col)
                    self.print_board()

                elif move_again == 'n':
                    break

                else:
                    print('Invalid answer, try again')

        return True

    def print_board(self):
        count = 0
        for row in self._board:
            print((str(count) + ': ') + str(row))
            count += 1


if __name__ == '__main__':
    c = Checkers()
    count = 0

    while c.get_game_state() == 'UNFINISHED':
        c.print_board()
        if count %2 == 0:
            player = 'X'
            from_row = int(input("Player X, from which row?"))
            from_col = int(input('Player X, from which col?'))
            

            if c.check_piece(player, from_row, from_col) == 'checker':
                to_row = int(input("Player X, to which row?"))
                to_col = int(input("Player X, to which col?"))
                if c.move_checker(player, from_row, from_col, to_row, to_col):
                    count += 1


        elif count % 2 != 0:
            player = 'O'
            from_row = int(input("Player O, from which row?"))
            from_col = int(input('Player O, from which col?'))

            if c.check_piece(player, from_row, from_col) == 'checker':
                to_row = int(input("Player O, to which row?"))
                to_col = int(input("Player O, to which col?"))
                if c.move_checker(player, from_row, from_col, to_row, to_col):
                    count += 1




