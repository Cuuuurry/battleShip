from player import Player
from ship import Ship


class LocationError(Exception):
    def __init__(self, reason: str) -> None:
        self.reason = reason

    def __str__(self) -> str:
        return self.reason


class OrientationError(Exception):
    def __init__(self, reason: str) -> None:
        self.reason = reason

    def __str__(self) -> str:
        return self.reason


class BoundError(Exception):
    def __init__(self, reason: str) -> None:
        self.reason = reason

    def __str__(self) -> str:
        return self.reason


class ShipOverlapError(Exception):
    def __init__(self, reason: str) -> None:
        self.reason = reason

    def __str__(self) -> str:
        return self.reason


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
        while True:
            try:
                type(x) == int
            except ValueError:
                print(" {} is not a valid value for row.\n It should be an integer "
                      "between 0 and {}.\n Please enter row again".format(x, board.num_rows - 1))
            else:
                break

        while True:
            try:
                type(y) == int
            except ValueError:
                print(" {} is not a valid value for col.\n It should be an integer "
                      "between 0 and {}.".format(y, board.num_cols - 1))
            else:
                break

    def location_fire_checking(self, x, y):
        """

        :param x:
        :param y:
        :return:
        """
        player = self.player
        board = player.scan_board
        opponent = self.opponent
        while True:
            try:
                board.is_in_bounds(x, y)
            except LocationError:
                print(f'{x}, {y} is not in bounds of our '
                      f'{board.num_rows} X {board.num_cols} board')
            else:
                break

        while True:
            # location have already fired
            try:
                board[x][y] = board.blank_char
            except LocationError:
                print(f"You have already fired at {x}, {y}")
            else:
                break

            board[[x, y]] = opponent.board[x][y]

    def coordinate_in_board_checking(self, x, y):
        # check the coordinate is valid or not
        board = self.player.board
        ship = self.ship
        while True:
            try:
                board.is_in_bounds(x, y)
            except LocationError:
                print("Cannot place {} {} at {}, {} "
                      "because it would be out of bounds."
                      .format(ship.ship_name, ship.ship_ori, x, y))
            else:
                break

    def ship_place_in_board_checking(self, x, y, is_vertical: bool):
        board = self.player.board
        ship = self.ship
        while True:
            try:
                bool((x + ship.ship_size - 1 > board.num_rows) * is_vertical +
                    (y + ship.ship_size - 1 > board.num_cols) * (1 - is_vertical))
            except BoundError:
                print("Cannot place {} {} at {}, {} "
                      "because it would be out of bounds.".format(ship.ship_name, ship.ship_ori, x, y))
            else:
                break

    def ship_place_conflict_checking(self, x, y, is_vertical: bool):
        board = self.player.board
        ship = self.ship
        while True:
            if not is_vertical:
                for row in range(x, x + ship.ship_size):
                    try:
                        board[[row, y]] = '0'
                    except ShipOverlapError:
                        print("Cannot place {} {} at {},{} because it would end up out of bounds."
                              .format(ship.ship_name, ship.ship_ori, x, y))
                    else:
                        break

            elif is_vertical:
                for col in range(y, y + ship.ship_size):
                    try:
                        board[[x, col]] = '0'
                    except ShipOverlapError:
                        print("Cannot place {} {} at {} {} because it would end up out of bounds."
                              .format(ship.ship_name, ship.ship_ori, x, y))
                    else:
                        break

    @staticmethod
    def location_length_checking(location):
        """

        :param location:
        :return:
        """
        # check valid location
        while True:
            try:
                row, col = location.split(',')
            except LocationError:
                print(f'{location} is not in the form row, col')
            else:
                break
