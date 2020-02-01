from player import Player
from ship import Ship


class Validation(object):
    def __init__(self, player: Player, opponent: Player, ship: Ship):
        self.player = player
        self.opponent = opponent
        self.ship = ship

    def location_type_checking(self, x, y, flag=False):
        """
        check whether row or col is an integer
        :param x: row
        :param y: col
        :param flag
        :return: bool
        """
        board = self.player.board
        try:
            x = int(x)
        except ValueError:
            print(" {} is not a valid value for row.\n It should be an integer "
                  "between 0 and {}.".format(x, board.num_rows - 1))
            flag = False
        else:
            flag = True

        try:
            y = int(y)
        except ValueError:
            print(" {} is not a valid value for col.\n It should be an integer "
                  "between 0 and {}.".format(y, board.num_cols - 1))
            flag = False
        else:
            flag = True and flag

        return flag

    def location_fire_checking(self, x, y, flag=False):
        """
        check fire location at board
        :param x: row
        :param y: col
        :param flag
        :return: bool
        """
        player = self.player
        board = player.scan_board
        opponent = self.opponent
        if not board.is_in_bounds(x, y):
            print(f'{x}, {y} is not in bounds of our '
                  f'{board.num_rows} X {board.num_cols} board')
            flag = False
        else:
            flag = True

        if board[[x, y]] != board.blank_char:
            print(f"You have already fired at {x}, {y}")
            flag = False
        else:
            flag = True and flag

        return flag

    def coordinate_in_board_checking(self, x, y):
        """
        check coordinate in board
        :param x: row
        :param y: col
        :return: bool
        """
        # check the coordinate is valid or not
        board = self.player.board
        ship = self.ship
        if not board.is_in_bounds(x, y):
            print("Cannot place {} {} at {}, {} "
                  "because it would be out of bounds."
                  .format(ship.ship_name, ship.ship_ori, x, y))
            return False
        else:
            return True

    def ship_place_in_board_checking(self, x, y, is_vertical: bool):
        """
        check ship place in board
        :param x: row
        :param y: col
        :param is_vertical: bool
        :return: bool
        """
        board = self.player.board
        ship = self.ship
        if not bool((x + ship.ship_size - 1 > board.num_rows) * is_vertical +
                (y + ship.ship_size - 1 > board.num_cols) * (1 - is_vertical)):
            print("Cannot place {} {} at {}, {} "
                  "because it would be out of bounds.".format(ship.ship_name, ship.ship_ori, x, y))
            return False
        else:
            return True

    def ship_place_conflict_checking(self, x, y, is_vertical: bool, flag=False):
        """
        check ship_place_conflict
        :param x: row
        :param y: col
        :param is_vertical: bool
        :param flag:
        :return: bool
        """
        board = self.player.board
        ship = self.ship
        if not is_vertical:
            for row in range(x, x + ship.ship_size):
                if board[[row, y]] != '0':
                    print("Cannot place {} {} at {},{} because it would end up out of bounds."
                          .format(ship.ship_name, ship.ship_ori, x, y))
                else:
                    flag = True

        elif is_vertical:
            for col in range(y, y + ship.ship_size):
                if board[[x, col]] != '0':
                    print("Cannot place {} {} at {} {} because it would end up out of bounds."
                          .format(ship.ship_name, ship.ship_ori, x, y))
                else:
                    flag = True and flag
        return flag

    @staticmethod
    def location_length_checking(location):
        """
        check length of input location
        :param location: ""
        :return: bool
        """
        # check valid location
        try:
            row, col = location.split(',')
        except ValueError:
            print(f'{location} is not in the form row, col')
            return False
        else:
            return True
