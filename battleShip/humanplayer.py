import heapq
from typing import List
from board import Board
import random
from checking import Validation
from ship import Ship
from player import Player


class HumanPlayer(Player):
    def __init__(self, listed_ships: List[Ship]):
        super().__init__(listed_ships)
        self.player_type = "human"

    def player_name_initializer(self, i: int) -> str:
        """
        Initialize the player's name
        :param i: int, refer to the 1st or 2nd player in the game.
        :return:
        """
        self.player_name = input(f"Player {i} please enter your name: ")
        return self.player_name

    def player_all_ships_initializer(self) -> None:
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
                                f"for the orientation of {ship.ship_name} which is {ship.ship_size} long: ")
            if ready_to_break:
                # check orientation validation and orientation setting
                if not ship.ship_oriented(orientation):
                    ready_to_break = False
                is_vertical = bool(ship.ship_ori == "vertical")

            if ready_to_break:
                location = input(f"{self.player_name}, enter the starting position for your {ship.ship_name} ship ,"
                                 f"which is {ship.ship_size} long, in the form row, column: ")

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
                vb = bool(col == y + size - 1)
                self.player_board_update(x, col, ship.ship_name[0].upper(), placement=True, verbose=vb)

        elif is_vertical:
            for row in range(x, x + size):
                vb = bool(row == x + size - 1)
                self.player_board_update(row, y, ship.ship_name[0].upper(), placement=True, verbose=vb)

        # update the location of the ship
        ship.ship_located((x, y))

        for loc in ship.ship_loc:
            heapq.heappush(self.player_ships_loc, loc)

    def ship_fire(self, opponent) -> None:
        board = self.scan_board
        ship = self.ship[0]
        test = Validation(board, ship)
        ready_to_break = False
        while not ready_to_break:
            location = input(f'{self.player_name}, enter the location you want to fire at in the form row, column: ')
            ready_to_break = True
            # location is not in the right length
            if ready_to_break:
                if not test.location_length_checking(location, fire=True):
                    ready_to_break = False
                else:
                    x, y = location.split(",")

            # location is invalid type
            if ready_to_break:
                if not test.location_type_checking(x, y, fire=True):
                    ready_to_break = False
                else:
                    x, y = int(x), int(y)

            # location is out of bound or conflict
            if ready_to_break:
                if not test.location_fire_checking(board, x, y):
                    ready_to_break = False

        if opponent.board[[x, y]] == opponent.board.blank_char:
            print("Miss")
            self.player_board_update(x, y, "O", scan=True, verbose=False)
            opponent.player_board_update(x, y, "O", verbose=False)
        else:
            fire_location = (x, y)
            for ship in opponent.ship:
                if fire_location in ship.ship_loc:
                    print("You hit {}'s {}!".format(opponent.player_name, ship.ship_name))
                    ship.ship_health_change()
                    if ship.ship_destroyed():
                        print("You destroyed {}'s {}".format(opponent.player_name, ship.ship_name))
                    opponent.player_health_change()
                    break
            self.player_board_update(x, y, "X", scan=True, verbose=False)
            opponent.player_board_update(x, y, "X", verbose=False)


if __name__ == "__main__":
    ship1 = Ship("monkey_1", 3)
    ship2 = Ship("monkey_2", 3)
    ship_list = [ship1, ship2]
    bob = HumanPlayer(ship_list)
    sally = HumanPlayer(ship_list)
    bob.player_board_initializer(5, 5)
    print(bob.ship)
    print(bob.board)
