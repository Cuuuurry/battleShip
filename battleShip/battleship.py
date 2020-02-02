"""
This File:
    Class battleShip for game process

"""
from sys import argv
from typing import Iterable, TypeVar, Tuple
from board import Board
from checking import Validation
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

    def game_backend_setup(self, ):
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
        while i <= 2:
            player = self.cur_player
            player.player_name_initializer(i)
            player.player_board_initializer(self.num_rows, self.num_cols)
            player.player_all_ships_initializer()
            player.player_health_initializer()
            self.change_turn()
            i += 1

    def ship_fire(self):
        player = self.cur_player
        board = player.scan_board
        opponent = self.cur_opponent
        ship = player.ship[0]
        test = Validation(board, ship)
        location = input('Pleas enter the location you wish to fire on: ')
        ready_to_break = False
        while not ready_to_break:
            ready_to_break = True
            # location is not in the right length
            if ready_to_break:
                if not test.location_length_checking(location):
                    location = input("please enter a new location")
                    ready_to_break = False
                else:
                    x, y = location.split(",")
            print("process 1 finished")

            # location is invalid type
            if ready_to_break:
                if not test.location_type_checking(x, y):
                    location = input("please enter a new location")
                    ready_to_break = False
                else:
                    x, y = int(x), int(y)
            print("process 2 finished")

            # location is out of bound
            if ready_to_break:
                if not test.location_fire_checking(board,x, y):
                    location = input("please enter a new location")
                    ready_to_break = False
            print("process 3 finished")

            player.scan_board[[x, y]] = opponent.board[[x, y]]

        fire_location = (x, y)
        miss = True
        for ship in opponent.ship:
            if fire_location in ship.ship_loc:
                player.fire_on_target(opponent.player_name, ship)
                ship.ship_health_change()
                if ship.ship_destroyed():
                    player.ship_status(opponent.player_name, ship)
                opponent.player_health_change()
                miss = False
        if miss:
            player.fire_miss()

    def change_turn(self):
        self.cur_player, self.cur_opponent = self.cur_opponent, self.cur_player

    def display_game_stat(self):
        cur_player = self.cur_player
        print(f"{cur_player.player_name}'s Scanning Board")
        print(cur_player.scan_board)
        print(f"{cur_player.player_name}'s Board")
        print(cur_player.board)

    def is_game_over(self):
        cur_opponent = self.cur_opponent
        if cur_opponent.player_health == 0:
            print("died")
            return True
        else:
            print("still alive")
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
        self.game_backend_setup()
        self.players_register()
        print(f"{self.cur_player.player_name} health is {self.cur_player.player_health}")
        print(f"{self.cur_opponent.player_name} health is {self.cur_opponent.player_health}")
        self.display_game_stat()
        self.ship_fire()
        print(self.cur_player.board)
        print(f"{self.cur_player.player_name} health is {self.cur_player.player_health}")
        print(f"{self.cur_opponent.player_name} health is {self.cur_opponent.player_health}")
        while not self.is_game_over():
            self.change_turn()
            self.display_game_stat()
            self.ship_fire()
            print(self.cur_player.board)
            print(f"{self.cur_player.player_name} health is {self.cur_player.player_health}")
            print(f"{self.cur_opponent.player_name} health is {self.cur_opponent.player_health}")
        self.display_the_winner()


if __name__ == "__main__":
    """ship_dict = {"P": 2, "U": 3}
    battle = BattleShip(9, 9, ship_dict)
    battle.play()"""
    ship_dict = {"Monkey": 1}
    battle = BattleShip(3, 4, ship_dict)
    battle.play()

