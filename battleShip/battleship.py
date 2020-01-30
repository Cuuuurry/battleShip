"""
This File:
    Class battleShip for game process

"""

from typing import Iterable, TypeVar
from board import Board
from player import Player
from ship import Ship
print("Successfully import classes")


class BattleShip(object):
    """
    Summary:
        Two players
        Four boards: two initial boards (static), two scan boards (dynamic)
    """
    def __init__(self, nrow, ncol, ship_size_dict) -> None:
        self.nrow = nrow
        self.ncol = ncol
        self.ship_size_dict = ship_size_dict
        self.board = {}
        for key in ["p1", "p2", "p1_scan", "p2_scan"]:
            self.board[key] = Board(nrow, ncol)
        self.players = [Player() for _ in range(2)]
        self.cur_player_turn = 0

    def load_ships(self, ship_name, location, orientation):
        '''Place ship of size, size, starting at position (x,y) and oriented
        vertically (oreitnation = 0) or horizontally (orientation = 1).'''
        size = self.ship_size_dict[ship_name]
        self.check_collisions(size, col, row, orientation)
        # Checks to make sure the ship doesn't lie outside the board and that
        # no ships have been placed on those spots.
        #check orientation validation
        if orientation.lower() in {"vertical", "v", "ve", "ver", "vert", "verti", "vertic", "vertica"}:
            isVertical = True
        elif orientation.lower() in {"horizontal", "h", "ho", "hor", "hori", "horiz", "horizo", "horizon",
                                     "horizont", "horizonta", "horizontal"}:
            isVertical = False
        else:
            raise Exception("{} does not represent an Orientation".format(orientation))

        #check valid location
        if len(location) != 2:
            raise Exception("{} is not in the form x, y.".format(location))

        col, row = location

        #check whether row or col is an integer
        if type(row) != int or row >= self.nrow or row < 0:
            raise Exception(" {} is not a valid value for row.\n It should be an integer "
                            "between 0 and {}.".format(row, self.nrow - 1))
        elif col >= self.ncol or col < 0 or type(col) != int:
            raise Exception(" {} is not a valid value for col.\n It should be an integer "
                            "between 0 and {}.".format(col, self.ncol - 1))

        #check The coordinate is out of bound
        if bool((row + size - 1 > self.nrow) * isVertical +
                (col + size - 1 > self.ncol) * (1 - isVertical)):
            raise Exception("Cannot place {} {} at {}, {} "
                            "because it would be out of bounds.".format(ship_name, orientation, row, col))

        if not isVertical:
            for x in range(col, col + size):
                self.board[x][row] = ship_name[0]
        elif isVertical:
            for y in range(row, row + size):
                self.board[col][y] = ship_name[0]

    def check_collisions(self, size, x, y, orientation):
        '''Checks to make sure the ship doesn't lie outside the board and that
        no ships have been placed on those spots.'''
        if not orientation:
            if self.size < (x + size) or self.size < y:
                raise OutofboardError()
            for x in range(x, x + size):
                if self.board.get((x, y)) != '.':
                    raise ShipAlreadyThere()
        elif orientation:
            if self.size < (y + size) or self.size < x:
                raise OutofboardError()
            for y in range(y, y + size):
                if self.board.get((x, y)) != '.':
                    raise ShipAlreadyThere()

    def fire(self):
        if not self.human:
            # checks to see if the current player should be a computer.
            x = random.randint(0, self.size)
            y = random.randint(0, self.size)
        else:
            x = raw_input('What is the x-coordinate you wish to fire on? ')
            y = raw_input('What is the y-coordinate you wish to fire on? ')
        try:
            x, y = int(x), int(y)
            # verifies that x and y are valid integers.
        except Exception:
            self.fire()
        self.fire_helper(x, y)

    def fire_helper(self, x, y):
        '''Fires at coordinates (x,y) on opponent'''

        if x > self.size or y > self.size:
            # Checks to make sure that x and y and in the scope of the board.
            print
            'Out of bounds'
            self.fire()
        elif self.opponents_board.get((x, y)) != '?':
            # Checks if the current spot has been chosen.
            print
            'That coordinate has been fired already'
            self.fire()
        elif (self.opponent.board.get((x, y)) == '.' or
              self.opponent.board.get((x, y)) == 'x'):
            # The player has hit an s and missed.
            print
            'Target missed'
            self.opponents_board[(x, y)] = 'x'
            self.opponent.board[(x, y)] = 'x'
        else:
            # A player's ship has been hit! Mark it on the board.
            ship_name_list = ['Destroyer', 'Frigate', 'Battleship', 'Carrier']

            print("Hit enemy's " + \
                  ship_name_list[self.opponent.board.get((x, y)) - 2])
            self.score -= 1
            self.opponents_board[(x, y)] = \
                self.opponent.board.get((x, y))
            self.opponent.board[(x, y)] = 'x'

    def turn(self):
        raw_input(self.name + ''''s turn''' + ' push enter to continue')
        if not self.human and self.opponent.human:
            pass
        else:
            print
            'Your board:'
            self.print_map(True)
            print
            '''Your view of your opponent's board:'''
            self.print_map(False)
            # Print your view of the opponents map.
        self.fire()
        for n in range(20):
            print('')

    def play(self) -> None:
        """
        Summary:
                Main loop of the game

        :return:
        """
        while not self.is_game_over():
            self.display_game_state()
            cur_player = self.get_cur_player()
            the_move = cur_player.get_move()
            the_move.make()
            self.change_turn()
        self.display_the_winner()

    def display_game_state(self) -> None:
        print(self.board)

    def is_game_over(self):
        return self.someone_won() or self.tie_game()

    def someone_won(self) -> bool:
        """

        :return:
        """

        return self.someone_won_horizontally() or self.someone_won_vertically() or self.someone_won_diagonally()

    def someone_won_horizontally(self) -> bool:
        for row in self.board:
            if all_same(row):
                return True
            else:
                return False

        # for i in range(self.board.rows):
        #     if self.board.row_all_same(self.board[i])
        #
        # do any of the rows
        # have all of the same characters
        return any(
            (all_same(row) for row in self.board)
        )

    # a b c
    # d e f
    # h i j



    def change_turn(self):
        self._cur_player_turn = (self._cur_player_turn + 1) % 2
        if self._cur_player_turn == 0:
            self._cur_player_turn = 1
        else:
            self._cur_player_turn = 0

    def get_cur_player(self):

        return self.players[self._cur_player_turn]