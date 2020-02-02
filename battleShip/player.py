""""
This File:
    Printout game information for players
"""
import sys
from typing import List
from checking import Validation
from ship import Ship
from board import Board


class Player(object):
    def __init__(self, listed_ships: List[Ship]) -> None:
        self.player_name = None
        self.ship = listed_ships  # list[ship]
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

    def player_board_update(self, x: int, y: int, char: str, placement=False, scan=False, verbose=True):
        if not scan and not placement:
            self.board[[x, y]] = char
            if verbose:
                print("{}'s Board".format(self.player_name))
                print(self.board)
        elif placement:
            self.board[[x, y]] = char
            if verbose:
                print("{}'s Placement Board".format(self.player_name))
                print(self.board)
        else:
            self.scan_board[[x, y]] = char
            if verbose:
                print("{}'s Scanning Board".format(self.player_name))
                print(self.scan_board)

    def player_all_ships_initializer(self):
        for ship in self.ship:
            self.player_single_ship_loader(ship)

    def player_single_ship_loader(self, ship: Ship) -> None:
        '''Place ship of size, size, starting at position (x,y) and oriented
        vertically (oreitnation = 0) or horizontally (orientation = 1).'''
        board = self.board
        size = ship.ship_size
        test = Validation(board, ship)

        ready_to_break = False
        # check valid location
        while not ready_to_break:
            ready_to_break = True
            orientation = input(f"{self.player_name} enter horizontal or vertical "
                                f"for the orientation of {ship.ship_name} which is {ship.ship_size} long:")
            if ready_to_break:
                # check orientation validation and orientation setting
                if not ship.ship_oriented(orientation):
                    ready_to_break = False
                is_vertical = bool(ship.ship_ori == "vertical")

            if ready_to_break:
                location = input(f"{self.player_name}, enter the starting position for your {ship.ship_name} ship ,"
                             f"which is {ship.ship_size} long, in the form row, column:")

            if ready_to_break:
                if not test.location_length_checking(location):
                    ready_to_break = False
                else:
                    x, y = location.split(',')

            # check whether row or col is an integer
            if ready_to_break:
                if not test.location_type_checking(x, y):
                    ready_to_break = False
                else:
                    x, y = int(x), int(y)

            # check the coordinate is valid or not
            if ready_to_break:
                if not test.coordinate_in_board_checking(x, y):
                    ready_to_break = False

            # check The ship is out of bound
            if ready_to_break:
                if not test.ship_place_in_board_checking(x, y, is_vertical):
                    ready_to_break = False

            # Checks to make sure the ship doesn't lie outside the board and that
            # no ships have been placed on those spots.
            if ready_to_break:
                if not test.ship_place_conflict_checking(x, y, is_vertical):
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


if __name__ == "__main__":
    ship1 = Ship("monkey_1", 3)
    ship2 = Ship("monkey_2", 3)
    ship_list = [ship1, ship2]
    bob = Player(ship_list)
    sally = Player(ship_list)
    print(bob)
