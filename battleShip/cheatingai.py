import heapq
from typing import List
from board import Board
import random
from checking import Validation
from ship import Ship
from player import Player


class CheatingAI(Player):
    def __init__(self, listed_ships):
        super().__init__(listed_ships)
        self.player_type = "CheatingAI"
        self.cheating_bag = []

    def cheating_name_initializer(self, i):
        self.player_name = f"Cheating AI {i}"
        return self.player_name

    def player_all_ships_initializer(self):
        for ship in self.ship:
            self.player_single_ship_loader(ship)
        return

    def player_single_ship_loader(self, ship: Ship):
        board = self.board
        size = ship.ship_size
        test = Validation(board, ship)

        ready_to_break = False
        while not ready_to_break:
            ready_to_break = True

            # setting orientation
            orientation = random.choice(["horizontal", "vertical"])
            ship.ship_oriented(orientation)
            is_vertical = bool(ship.ship_ori == "vertical")

            x = random.randint(0, board.num_rows - 1 - (ship.ship_size - 1) * is_vertical)
            y = random.randint(0, board.num_cols - 1 - (ship.ship_size - 1) * (1 - is_vertical))

            # Checks to make sure the ship doesn't lie outside the board and that
            # no ships have been placed on those spots.
            if ready_to_break:
                if not test.ship_place_conflict_checking(x, y, is_vertical, verbose=False):
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
        return

    def cheating_bag_initializer(self, opponent):
        self.cheating_bag = opponent.player_ships_loc

    def ship_fire(self, opponent) -> None:
        if not self.cheating_bag:
            raise Exception("We should have won!")
            return
        x, y = heapq.heappop(self.cheating_bag)
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
        return
