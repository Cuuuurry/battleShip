from player import Player
from ship import Ship


class Validation(object):
    def __init__(self, player: Player, opponent: Player, ship: Ship):
        self.player = player
        self.opponent = opponent
        self.ship = ship

    def location_type_checking(self, x, y):
        """
        check whether row or col is an integer
        :param x: row
        :param y: col
        :return: checking info: ValueError
        """
        board = self.player.board
        if x != int(x):
            print(" {} is not a valid value for row.\n It should be an integer "
                  "between 0 and {}.".format(x, board.num_rows - 1))

        elif y != int(y):
            print(" {} is not a valid value for col.\n It should be an integer "
                  "between 0 and {}.".format(y, board.num_cols - 1))
        else:
            pass
        return x != int(x) or y != int(y)

    def location_fire_checking(self, x, y):
        """

        :param x:
        :param y:
        :return:
        """
        player = self.player
        board = player.scan_board
        opponent = self.opponent
        if board.is_in_bounds(x, y) is not True:
            print(f'{x}, {y} is not in bounds of our '
                  f'{board.num_rows} X {board.num_cols} board')

        elif board[x][y] != board.blank_char:
            print(f"You have already fired at {x}, {y}")

        else:
            board[[x, y]] = opponent.board[x][y]
            pass

    def coordinate_in_board_checking(self, x, y):
        # check the coordinate is valid or not
        board = self.player.board
        ship = self.ship
        if board.is_in_bounds(x, y) is not True:
            print("Cannot place {} {} at {}, {} "
                  "because it would be out of bounds."
                  .format(ship.ship_name, ship.ship_ori, x, y))
        else:
            pass

    def ship_place_in_board_checking(self, x, y, is_vertical: bool):
        board = self.player.board
        ship = self.ship
        if bool((x + ship.ship_size - 1 > board.num_rows) * is_vertical +
                (y + ship.ship_size - 1 > board.num_cols) * (1 - is_vertical)) is not True:
            print("Cannot place {} {} at {}, {} "
                  "because it would be out of bounds.".format(ship.ship_name, ship.ship_ori, x, y))
        else:
            return True

    def ship_place_conflict_checking(self, x, y, is_vertical: bool):
        board = self.player.board
        ship = self.ship
        if not is_vertical:
            for row in range(x, x + ship.ship_size):
                if board[[row, y]] != '0':
                    print("Cannot place {} {} at {},{} because it would end up out of bounds."
                          .format(ship.ship_name, ship.ship_ori, x, y))

        elif is_vertical:
            for col in range(y, y + ship.ship_size):
                if board[[x, col]] != '0':
                    print("Cannot place {} {} at {} {} because it would end up out of bounds."
                          .format(ship.ship_name, ship.ship_ori, x, y))
                else:
                    return True

    @staticmethod
    def location_length_checking(location):
        """

        :param location:
        :return:
        """
        # check valid location
        try:
            row, col = location.split(',')
        except ValueError:
            print(f'{location} is not in the form row, col')
            return False
        else:
            return True
