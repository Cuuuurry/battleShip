""""
This File:
    Printout game information for players
"""
import sys
import typing

from checking import Validation
from ship import Ship
from board import Board


class Player(object):
    def __init__(self, ship_list) -> None:
        self.player_name = None
        self.ship = ship_list  # list[ship]
        self.board = None
        self.scan_board = None
        self.player_health = 0

    def __str__(self) -> str:
        return self.player_name

    def player_name_initializer(self, i):
        self.player_name = input(f"Player {i} please enter your name: ")

    def player_board_initializer(self, num_rows: int, num_cols: int, blank_char: str = "*"):
        self.board = Board(num_rows, num_cols, blank_char)
        self.scan_board = Board(num_rows, num_cols, blank_char)
        print("{}'s Placement Board".format(self.player_name))
        print(self.board)

    def player_board_update(self, x: int, y: int, char: str, placement=False, scan=False):
        if not scan and not placement:
            self.board[[x, y]] = char
            print("{}'s Board".format(self.player_name))
            print(self.board)
        elif placement:
            self.board[[x, y]] = char
            print("{}'s Placement Board".format(self.player_name))
            print(self.board)
        else:
            self.scan_board[[x, y]] = char
            print("{}'s Scanning Board".format(self.player_name))

    def player_all_ships_initializer(self):
        for ship in self.ship:
            self.player_single_ship_loader(ship)

    def player_single_ship_loader(self, ship: Ship) -> None:
        '''Place ship of size, size, starting at position (x,y) and oriented
        vertically (oreitnation = 0) or horizontally (orientation = 1).'''
        board = self.board
        size = ship.ship_size
        test = Validation(board, ship)
        orientation = input(f"{self.player_name} enter horizontal or vertical "
                            f"for the orientation of {ship.ship_name} which is {ship.ship_size} long:")

        # check orientation validation and orientation setting
        ship.ship_oriented(orientation)
        is_vertical = bool(ship.ship_ori == "vertical")

        location = input(f"{self.player_name}, enter the starting position for your {ship.ship_name} ship ,"
                         f"which is {ship.ship_size} long, in the form row, column:")

        ready_to_break = False
        # check valid location
        while not ready_to_break:
            ready_to_break = True
            if ready_to_break:
                if not test.location_length_checking(location):
                    location = input("Please 1")
                    ready_to_break = False
                else:
                    x, y = location.split(',')

        # check whether row or col is an integer
            if ready_to_break:
                if not test.location_type_checking(x, y):
                    location = input("Please 2")
                    ready_to_break = False
                else:
                    x, y = int(x), int(y)

        # check the coordinate is valid or not
            if ready_to_break:
                if not test.coordinate_in_board_checking(x, y):
                    location = input("Please 3")
                    ready_to_break = False

        # check The ship is out of bound
            if ready_to_break:
                if not test.ship_place_in_board_checking(x, y, is_vertical):
                    location = input("Please 4")
                    ready_to_break = False

        # Checks to make sure the ship doesn't lie outside the board and that
        # no ships have been placed on those spots.
            if ready_to_break:
                if not test.ship_place_conflict_checking(x, y, is_vertical):
                    location = input("Please 5")
                    ready_to_break = False

        # store ship message on board:
        if not is_vertical:
            for col in range(y, y + size):
                self.player_board_update(x, col, ship.ship_name[0].upper(), placement=True)

        elif is_vertical:
            for row in range(x, x + size):
                self.player_board_update(row, y, ship.ship_name[0].upper(), placement=True)

        # update the location of the ship
        ship.ship_located((x, y))

    def player_health_initializer(self, ):
        for ship in self.ship:
            self.player_health += ship.ship_health
        return self.player_health

    def player_health_change(self, ):
        self.player_health -= 1

    def load_info(self, ):
        print("{} enter horizontal or vertical for the {} of {} which is {} long: ".format(
            self.player_name, self.ship_ori, self.ship_name, self.ship_size
        ))

        print("{}, enter the starting position for your {} ship ,which is {} long, in the form {}, {}: ".format(
            self.player_name, self.ship_name, self.ship_size, self.ship_loc[1], self.ship_loc[0]
        ))

        print("{}'s Placement Board".format(self.player_name))

    def status_info(self,):
        print("{}'s Board: ".format(self.player_name))

    def status_scan_info(self):
        print("{}'s Scanning Board: ".format(self.player_name))

    def fire_info(self, ):
        print("{}, enter the location you want to fire at in the form {}, {}: ".format(
            self.player_name, self.ship_loc[1], self.ship_loc[0]))

    @staticmethod
    def fire_miss():
        print("Miss")

    @staticmethod
    def fire_on_target(opponent_name, ship: Ship):
        print("You hit {}'s {}!".format(opponent_name, ship.ship_name))

    @staticmethod
    def ship_status(opponent_name, ship: Ship):
        print("You destroyed {}'s {}".format(opponent_name, ship.ship_name))

    def game_result(self, ):
        print("{} won the game!".format(self.player_name))


if __name__ == "__main__":
    ship1 = Ship("monkey_1", 3)
    ship2 = Ship("monkey_2", 3)
    ship_list = [ship1, ship2]
    bob = Player(ship_list)
    sally = Player(ship_list)
    bob.player_info(1)
    print(bob)
