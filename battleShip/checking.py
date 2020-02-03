from board import Board
from ship import Ship


class Validation(object):
    def __init__(self, board: Board, ship: Ship):
        self.board = board
        self.ship = ship

    def location_type_checking(self, x: str, y: str, fire=False):
        """
        check whether row or col is an integer
        :param fire:
        :param x: row
        :param y: col
        :param flag
        :return: bool
        """
        board = self.board
        try:
            x = int(x)
        except ValueError:
            if not fire:
                print(f"{x} is not a valid value for row.")
                print(f"It should be an integer between 0 and {board.num_rows - 1}")
            else:
                print(f"Row should be an integer. {x} is NOT an integer.")
            return False

        try:
            y = int(y)
        except ValueError:
            if not fire:
                print(f"{y} is not a valid value for col.")
                print(f"It should be an integer between 0 and {board.num_cols - 1}")
            else:
                print(f"Column should be an integer. {y} is NOT an integer.")
            return False

        return True

    def coordinate_in_board_checking(self, x, y):
        """
        check coordinate in board
        :param x: row
        :param y: col
        :return: bool
        """
        # check the coordinate is valid or not
        board = self.board
        ship = self.ship
        if not board.is_in_bounds(x, y):
            print("Cannot place {} {}ly at {}, {} "
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
        board = self.board
        ship = self.ship
        if bool((x + ship.ship_size > board.num_rows) * is_vertical +
                (y + ship.ship_size > board.num_cols) * (1 - is_vertical)):
            print("Cannot place {} {}ly at {}, {} "
                  "because it would end up out of bounds.".format(ship.ship_name, ship.ship_ori, x, y))
            return False
        else:
            return True

    def ship_place_conflict_checking(self, x: int, y: int, is_vertical: bool, flag=False):
        """
        check ship_place_conflict
        :param x: row
        :param y: col
        :param is_vertical: bool
        :param flag:
        :return: bool
        """
        board = self.board
        ship = self.ship
        if is_vertical:
            for row in range(x, x + ship.ship_size):
                if board[[row, y]] != '*':
                    print("Cannot place {} {}ly at {}, {} because it would overlap with [\'{}\']"
                          .format(ship.ship_name, ship.ship_ori, x, y, board[[row, y]]))
                    flag = False
                    break
                else:
                    flag = True
        elif not is_vertical:
            for col in range(y, y + ship.ship_size):
                if board[[x, col]] != '*':
                    print("Cannot place {} {}ly at {}, {} because it would overlap with [\'{}\']"
                          .format(ship.ship_name, ship.ship_ori, x, y, board[[x, col]]))
                    flag = False
                    break
                else:
                    flag = True
        return flag

    @staticmethod
    def location_length_checking(location: str, fire=False):
        """
        check length of input location
        :param fire:
        :param location: ""
        :return: bool
        """
        # check valid location
        try:
            row, col = location.split(',')
        except ValueError:
            if not fire:
                print(f'{location} is not in the form x,y')
            else:
                print(f"{location} is not a valid location.")
                print("Enter the firing location in the form row, column")
            return False
        else:
            return True

    @staticmethod
    def location_fire_checking(board: Board, x: int, y: int):
        """
        check fire location at board
        :param board:
        :param x: row
        :param y: col
        :return: bool
        """
        if not board.is_in_bounds(x, y):
            print(f'{x}, {y} is not in bounds of our '
                  f'{board.num_rows} X {board.num_cols} board.')
            flag = False
        elif board[[x, y]] != board.blank_char:
            print(f"You have already fired at {x}, {y}.")
            flag = False
        else:
            flag = True

        return flag
