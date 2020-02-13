""""
This File:
    Printout game information for players
"""
import sys
from typing import List
from checking import Validation
from ship import Ship
from board import Board
import heapq

class Player(object):
    def __init__(self, listed_ships: List[Ship]) -> None:
        self.player_name = None
        self.ship = listed_ships  # list[ship]
        self.board = None
        self.scan_board = None
        self.player_health = 0
        self.player_ships_loc = []

    def __str__(self) -> str:
        return self.player_name

    def player_board_initializer(self, num_rows: int, num_cols: int, blank_char: str = "*") -> None:
        """

        :param num_rows: int
        :param num_cols: int
        :param blank_char: str
        :return: None
        """
        self.board = Board(num_rows, num_cols, blank_char)
        self.scan_board = Board(num_rows, num_cols, blank_char)
        print("{}'s Placement Board".format(self.player_name))
        print(self.board)

    def player_board_update(self, x: int, y: int, char: str, placement=False, scan=False, verbose=True) -> None:
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

    def player_health_initializer(self) -> int:
        for ship in self.ship:
            self.player_health += ship.ship_health
        return self.player_health

    def player_health_change(self) -> None:
        self.player_health -= 1


if __name__ == "__main__":
    ship1 = Ship("monkey_1", 3)
    ship2 = Ship("monkey_2", 3)
    ship_list = [ship1, ship2]
    bob = Player(ship_list)
    sally = Player(ship_list)