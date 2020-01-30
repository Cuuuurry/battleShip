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
        self.players = [Player() for _ in range(2)]
        self.cur_player_turn = 0

    def load_ship(self, ship: Ship, player: Player, orientation, location):
        '''Place ship of size, size, starting at position (x,y) and oriented
        vertically (oreitnation = 0) or horizontally (orientation = 1).'''
        board = player.board
        size = ship.ship_size

        # check orientation validation and orientation setting
        ship.ship_oriented(orientation)
        is_vertical = bool(ship.ship_ori == "vertical")

        # check valid location
        if len(location) != 2:
            raise Exception("{} is not in the form x, y.".format(location))

        col, row = location

        # check whether row or col is an integer
        if type(row) != int:
            raise Exception(" {} is not a valid value for row.\n It should be an integer "
                            "between 0 and {}.".format(row, self.nrow - 1))
        elif type(col) != int:
            raise Exception(" {} is not a valid value for col.\n It should be an integer "
                            "between 0 and {}.".format(col, self.ncol - 1))

        # check the coordinate is valid or not
        if col >= self.ncol or col < 0 or row >= self.nrow or row < 0:
            raise Exception("Cannot place {} {} at {}, {} "
                            "because it would be out of bounds."
                            .format(ship.ship_name, orientation, col, row))

        # check The ship is out of bound
        if bool((row + size - 1 > self.nrow) * is_vertical +
                (col + size - 1 > self.ncol) * (1 - is_vertical)):
            raise Exception("Cannot place {} {} at {}, {} "
                            "because it would be out of bounds.".format(ship.ship_name, orientation, col, row))

        # Checks to make sure the ship doesn't lie outside the board and that
        # no ships have been placed on those spots.
        if not is_vertical:
            for x in range(row, row + size):
                if board[x][col] != '*':
                    raise Exception("Cannot place {} {} at {},{} because it would end up out of bounds."
                                    .format(ship.ship_name, orientation, row, col))
        elif is_vertical:
            for y in range(col, col + size):
                if board[row][y] != '*':
                    raise Exception("Cannot place {} {} at {} {} because it would end up out of bounds."
                                    .format(ship.ship_name, orientation, row, col))

        if not is_vertical:
            for x in range(row, row + size):
                board[x][col] = ship.ship_name[0]
        elif is_vertical:
            for y in range(col, col + size):
                board[row][y] = ship.ship_name[0]

    def load_ships(self):
        for player in self.players:
            for ship in player.ship:
                orientation = input("Please enter orientation here")
                location = input("Please enter location here")
                self.load_ship(ship, player, orientation, location)




    def ship_fire(self, location):
        x = input('What is the x-coordinate you wish to fire on? ')
        y = input('What is the y-coordinate you wish to fire on? ')
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

    def change_turn(self):
        input(self.name + ''''s turn''' + ' push enter to continue')
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
        self._cur_player_turn = (self._cur_player_turn + 1) % 2
        if self._cur_player_turn == 0:
            self._cur_player_turn = 1
        else:
            self._cur_player_turn = 0

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








    def get_cur_player(self):

        return self.players[self._cur_player_turn]