import heapq
from typing import List
from board import Board
import random
from checking import Validation
from ship import Ship
from player import Player


class SearchDestroyAi(Player):
    def __init__(self, listed_ships: List[Ship]):
        super().__init__(listed_ships)
        self.player_type = "SearchDestroyAI"
        self.mode = "Search"
        self.target_points_queue = []  # the current place, the current ship,

    def SD_name_initializer(self, i: int):
        self.player_name = f"Search Destroy AI {i}"
        return self.player_name

    def player_all_ships_initializer(self):
        for ship in self.ship:
            self.player_single_ship_loader(ship)
        return

    def player_single_ship_loader(self, ship: Ship):
        board = self.board
        size = ship.ship_size
        test = Validation(board, ship)

        while not ready_to_break:
            ready_to_break = True

            # setting orientation
            orientation = random.choice(["horizontal", "vertical"])
            ship.ship_oriented(orientation)
            is_vertical = bool(ship.ship_ori == "vertical")

            x = random.randint(0, board.num_rows - ship.ship_size * (1 - is_vertical))
            y = random.randint(0, board.num_cols - ship.ship_size * is_vertical)

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
            heapq.heappush(self.player_remain_loc, loc)
        return

    def ship_fire(self, opponent) -> None:
        board = self.scan_board
        ship = self.ship[0]
        test = Validation(board, ship)
        ready_to_break = False
        while not ready_to_break:
            if not self.target_points_queue:
                self.mode = "Search"
            if self.mode == "Search":
                x = random.randint(0, board.num_rows - 1)
                y = random.randint(0, board.num_cols - 1)
            else:
                x, y = self.target_points_queue.pop(0)
            ready_to_break = True
            # location is out of bound or conflict
            if ready_to_break:
                if not test.location_fire_checking(board, x, y, verbose=False):
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
            if x > 0:
                self.target_points_queue.append([x - 1, y])
            if y > 0:
                self.target_points_queue.append([x, y - 1])
            if x + 1 < board.num_rows:
                self.target_points_queue.append([x + 1, y])
            if y + 1 < board.num_cols:
                self.target_points_queue.append([x, y + 1])

            self.mode = "Destroy"

            self.player_board_update(x, y, "X", scan=True, verbose=False)
            opponent.player_board_update(x, y, "X", verbose=False)
