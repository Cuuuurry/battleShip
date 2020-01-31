"""
This File:
    Class battleShip for game process

"""
from sys import argv
from typing import Iterable, TypeVar, Tuple
from board import Board
from checking import LocationError, Validation
from player import Player
from ship import Ship
print("Successfully import classes")


class BattleShip(object):
    """
    Summary:
        Two players
        Four boards: two initial boards (static), two scan boards (dynamic)
    """
    def __init__(self, num_rows, num_cols, ship_size_dict) -> None:
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.players = []
        self.cur_player = None
        self.cur_opponent = None
        self.ship_size_dict = ship_size_dict

    def ship_dict_loading(self, ):
        ship_size_dict = self.ship_size_dict
        ship_list = []
        for ship_name, ship_size in ship_size_dict.items():
            new_ship = Ship(ship_name, int(ship_size))
            ship_list.append(new_ship)
        for i in range(2):
            new_player = Player(ship_list)
            self.players.append(new_player)
        self.cur_player, self.cur_opponent = self.players

    def players_register(self) -> None:
        i = 1
        for player in self.players:
            player.player_info(i)
            player.board = Board(self.num_rows, self.num_cols, blank_char="0")
            print(player.board)
            player.scan_board = Board(self.num_rows, self.num_cols)
            i += 1

    def load_ship(self, ship: Ship, orientation: str, location: str) -> None:
        '''Place ship of size, size, starting at position (x,y) and oriented
        vertically (oreitnation = 0) or horizontally (orientation = 1).'''
        player = self.cur_player
        opponent = self.cur_opponent
        board = player.board
        size = ship.ship_size

        # check orientation validation and orientation setting
        ship.ship_oriented(orientation)
        is_vertical = bool(ship.ship_ori == "vertical")

        # check valid location
        test = Validation(player, opponent, ship)
        test.location_length_checking(location)
        x, y = location.split(',')

        # check whether row or col is an integer
        test.location_type_checking(x, y)
        x, y = int(x), int(y)

        # check the coordinate is valid or not
        test.coordinate_in_board_checking(x, y)

        # check The ship is out of bound
        test.ship_place_in_board_checking(x, y, is_vertical)

        # Checks to make sure the ship doesn't lie outside the board and that
        # no ships have been placed on those spots.
        test.ship_place_conflict_checking(x, y, is_vertical)

        if not is_vertical:
            for col in range(y, y + size):
                board[[x, col]] = ship.ship_name[0]
        elif is_vertical:
            for row in range(x, x + size):
                board[[row, y]] = ship.ship_name[0]
        # update the location of the ship
        ship.ship_located((x, y))

    def load_all_ships(self):
        for i in range(2):
            player = self.cur_player
            for ship in player.ship:
                orientation = input("Please enter orientation here: ")
                location = input("Please enter location here: ")
                self.load_ship(ship, orientation, location)
            self.change_turn()

    def initial_all_stats(self):
        for player in self.players:
            player.player_health_initializer()


    def ship_fire(self):
        location = input('Pleas enter the location you wish to fire on: ')
        # location is not in the right length
        player = self.cur_player
        opponent = self.cur_opponent
        ship = player.ship[0]
        test = Validation(player, opponent, ship)
        test.location_length_checking(location)
        x, y = location.split(",")

        # location is invalid type
        test.location_type_checking(x, y)
        x, y = int(x), int(y)

        # location is out of bound
        if not player.scan_board.is_in_bounds(x, y):
            raise LocationError(f'{x}, {y} is not in bounds of our '
                                f'{player.scan_board.num_rows} X {player.scan_board.num_cols} board')
        # location have already fired
        elif player.scan_board[[x, y]] != player.scan_board.blank_char:
            raise LocationError(f"You have already fired at {x}, {y}")
        else:
            player.scan_board[[x, y]] = opponent.board[[x, y]]

        fire_location = (x, y)
        miss = True
        for ship in opponent.ship:
            if fire_location in ship.ship_loc:
                player.fire_on_target(opponent.player_name, ship)
                ship.ship_health_change()
                if ship.ship_destroyed():
                    player.ship_status(opponent.player_name, ship)
                player.player_health_change()
                miss = False
        if miss:
            player.fire_miss()

    def change_turn(self):
        self.cur_player, self.cur_opponent = self.cur_opponent, self.cur_player

    def display_game_stat(self):
        cur_player = self.cur_player
        print(cur_player.board)
        print(cur_player.scan_board)


    def is_game_over(self):
        cur_opponent = self.cur_opponent
        if not cur_opponent.player_health:
            return True
        else:
            return False

    def display_the_winner(self):
        print(self.cur_player)

    def play(self) -> None:
        """
        Summary:
                Main loop of the game

        :return:
        """
        # setups
        self.ship_dict_loading()
        self.players_register()
        self.load_all_ships()
        self.initial_all_stats()
        self.display_game_stat()
        self.ship_fire()
        while not self.is_game_over():
            self.change_turn()
            self.display_game_stat()
            self.ship_fire()
            print(self.cur_player.board)
        self.display_the_winner()


if __name__ == "__main__":
    ship_dict = {"P": 3, "U":2}
    battle = BattleShip(9, 9, ship_dict)
    battle.play()
    print(self.cur_player.name)
    print(self.cur_opponent.name)