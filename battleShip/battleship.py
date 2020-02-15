"""
This File:
    Class battleShip for game process

"""
from typing import Dict
from cheatingai import CheatingAI
from humanplayer import HumanPlayer
from randomai import RandomAI
from searchdestroyplayer import SearchDestroyAi
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

    def players_register(self) -> None:
        ship_size_dict = self.ship_size_dict
        for i in range(1, 3):
            ship_list = []
            for ship_name, ship_size in ship_size_dict.items():
                new_ship = Ship(ship_name, int(ship_size))
                ship_list.append(new_ship)
            name_unique = False

            type_of_player = input(f"Enter one of ['Human', 'CheatingAi', "
                                   f"'SearchDestroyAi', 'RandomAi'] for Player {i}'s type: ")
            type_of_player = type_of_player.strip().lower()
            compare_num = len(type_of_player)

            if type_of_player == "human"[:compare_num]:
                player = HumanPlayer(ship_list)
                while not name_unique:
                    name = player.player_name_initializer(i)
                    if name not in self.player_name_pool:
                        name_unique = True
                        self.player_name_pool.add(name)
                    else:
                        print(f"Someone is already using {name} for their name.")
                        print("Please choose another name.")

            else:
                if type_of_player == "randomai"[:compare_num]:
                    player = RandomAI(ship_list)
                    name = player.random_name_initializer(i)
                elif type_of_player == "searchdestroyai"[:compare_num]:
                    player = SearchDestroyAi(ship_list)
                    name = player.SD_name_initializer(i)
                elif type_of_player == "cheatingai"[:compare_num]:
                    player = CheatingAI(ship_list)
                    name = player.cheating_name_initializer(i)

                self.player_name_pool.add(name)

            self.players.append(player)
            player.player_board_initializer(self.num_rows, self.num_cols)
            player.player_all_ships_initializer()
            player.player_health_initializer()

        self.cur_player, self.cur_opponent = self.players

        # if you are cheater AI, we show you the ability to cheat
        if self.cur_player.player_type == "CheatingAI":
            self.cur_player.cheating_bag = self.cur_opponent.player_ships_loc

        if self.cur_opponent.player_type == "CheatingAI":
            self.cur_opponent.cheating_bag = self.cur_player.player_ships_loc

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
        # setups1
        self.players_register()
        self.display_game_stat()
        self.cur_player.ship_fire(self.cur_opponent)
        self.display_game_stat()
        while not self.is_game_over():
            self.change_turn()
            self.display_game_stat()
            self.cur_player.ship_fire(self.cur_opponent)
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


