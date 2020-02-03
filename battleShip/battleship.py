"""
This File:
    Class battleShip for game process

"""
from sys import argv
from typing import Iterable, TypeVar, Tuple, Dict
from checking import Validation
from player import Player
from ship import Ship


class BattleShip(object):
    """
    Summary:
        Two players
        Four boards: two initial boards (static), two scan boards (dynamic)
    """
    def __init__(self, num_rows: int, num_cols: int, ship_size_dict: Dict) -> None:
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.players = []
        self.player_name_pool = set()
        self.cur_player = None
        self.cur_opponent = None
        self.ship_size_dict = ship_size_dict

    def game_backend_setup(self) -> None:
        ship_size_dict = self.ship_size_dict
        for i in range(2):
            ship_list = []
            for ship_name, ship_size in ship_size_dict.items():
                new_ship = Ship(ship_name, int(ship_size))
                ship_list.append(new_ship)
            new_player = Player(ship_list)
            self.players.append(new_player)
        self.cur_player, self.cur_opponent = self.players

    def players_register(self) -> None:
        i = 1
        while i <= 2:
            player = self.cur_player
            name_unique = False
            while not name_unique:
                name = player.player_name_initializer(i)
                if name not in self.player_name_pool:
                    name_unique = True
                    self.player_name_pool.add(name)
                else:
                    print(f"Someone is already using {name} for their name.")
                    print("Please choose another name.")
            player.player_board_initializer(self.num_rows, self.num_cols)
            player.player_all_ships_initializer()
            player.player_health_initializer()
            self.change_turn()
            i += 1

    def ship_fire(self) -> None:
        player = self.cur_player
        board = player.scan_board
        opponent = self.cur_opponent
        ship = player.ship[0]
        test = Validation(board, ship)
        ready_to_break = False
        while not ready_to_break:
            location = input(f'{player.player_name}, enter the location you want to fire at in the form row, column: ')
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
            player.player_board_update(x, y, "O", scan=True, verbose=False)
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
            player.player_board_update(x, y, "X", scan=True, verbose=False)
            opponent.player_board_update(x, y, "X", verbose=False)

    def change_turn(self) -> None:
        self.cur_player, self.cur_opponent = self.cur_opponent, self.cur_player

    def display_game_stat(self) -> None:
        cur_player = self.cur_player
        print(f"{cur_player.player_name}'s Scanning Board")
        print(cur_player.scan_board )
        print("")
        print(f"{cur_player.player_name}'s Board")
        print(cur_player.board)
        print("")

    def is_game_over(self) -> bool:
        cur_opponent = self.cur_opponent
        if cur_opponent.player_health == 0:
            return True
        else:
            return False

    def display_the_winner(self) -> None:
        print("{} won the game!".format(self.cur_player.player_name))

    def play(self) -> None:
        """
        Summary:
                Main loop of the game

        :return:
        """
        # setups
        self.game_backend_setup()
        self.players_register()
        self.display_game_stat()
        self.ship_fire()
        self.display_game_stat()
        while not self.is_game_over():
            self.change_turn()
            self.display_game_stat()
            self.ship_fire()
            self.display_game_stat()
        self.display_the_winner()


if __name__ == "__main__":
    """ship_dict = {"P": 2, "U": 3}
    battle = BattleShip(9, 9, ship_dict)
    battle.play()"""
    case = input("please input a number from 1 to 5")
    if case == "1":
        # test case 1:
        ship_dict = {"Patrol": 2, "Submarine": 3}
        battle = BattleShip(5, 6, ship_dict)
        battle.play()
    elif case == "2":
        # test case 2:
        ship_dict = {"Patrol": 2, "Submarine": 3, "Destroyer": 3, "Battleship": 4, "Carrier": 5}
        battle = BattleShip(7, 7, ship_dict)
        battle.play()
    elif case == "3":
        # test case 3:
        ship_dict = {"Patrol": 2, "Submarine": 3}
        battle = BattleShip(5, 6, ship_dict)
        battle.play()
    elif case == "4":
        # test case 4:
        ship_dict = {"Monkey": 1}
        battle = BattleShip(3, 4, ship_dict)
        battle.play()
    elif case == "5":
        # the case for ship placement checking(case 5 in text)
        ship_dict = {"Patrol": 2, "Submarine": 3}
        battle = BattleShip(5, 6, ship_dict)
        battle.play()


