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


class Validation(object):
    def __init__(self, player: Player, opponent: Player, ship: Ship):
        self.player = player
        self.opponent = opponent
        self.ship = ship

    def location_type_checking(self, x, y):
        # check whether row or col is an integer
        board = self.player.board
        try:
            x = int(x)
        except ValueError:
            raise Exception(" {} is not a valid value for row.\n It should be an integer "
                            "between 0 and {}.".format(x, board.num_rows - 1))

        try:
            y = int(y)
        except ValueError:
            raise Exception(" {} is not a valid value for col.\n It should be an integer "
                            "between 0 and {}.".format(y, board.num_cols - 1))

    def location_fire_checking(self, x, y):
        player = self.player
        board = player.scan_board
        opponent = self.opponent
        if not board.is_in_bounds(x, y):
            raise LocationError(f'{x}, {y} is not in bounds of our '
                                f'{board.num_rows} X {board.num_cols} board')
        # location have already fired
        elif board[x][y] != board.blank_char:
            raise LocationError(f"You have already fired at {x}, {y}")
        else:
            board[[x, y]] = opponent.board[x][y]


    def coordinate_in_board_checking(self, x, y):
        # check the coordinate is valid or not
        board = self.player.board
        ship = self.ship

        if not board.is_in_bounds(x, y):
            raise LocationError("Cannot place {} {} at {}, {} "
                                "because it would be out of bounds."
                                .format(ship.ship_name, ship.ship_ori, x, y))

    def ship_place_in_board_checking(self, x, y, is_vertical: bool):
        board = self.player.board
        ship = self.ship

        if bool((x + ship.ship_size - 1 > board.num_rows) * is_vertical +
                (y + ship.ship_size - 1 > board.num_cols) * (1 - is_vertical)):
            raise Exception("Cannot place {} {} at {}, {} "
                            "because it would be out of bounds.".format(ship.ship_name, ship.ship_ori, x, y))

    def ship_place_conflict_checking(self, x, y, is_vertical: bool):
        board = self.player.board
        ship = self.ship

        if not is_vertical:
            for row in range(x, x + ship.ship_size):
                if board[[row, y]] != '*':
                    raise Exception("Cannot place {} {} at {},{} because it would end up out of bounds."
                                    .format(ship.ship_name, ship.ship_ori, x, y))

        elif is_vertical:
            for col in range(y, y + ship.ship_size):
                if board[[x, col]] != '*':
                    raise Exception("Cannot place {} {} at {} {} because it would end up out of bounds."
                                    .format(ship.ship_name, ship.ship_ori, x, y))


    @staticmethod
    def location_length_checking(location):
        # check valid location
        try:
            row, col = location.split(',')
        except LocationError:
            raise Exception(f'{location} is not in the form row, col')
