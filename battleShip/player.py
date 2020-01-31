""""
This File:
    Printout game information for players
"""
import sys
import typing

from ship import Ship


class Player(object):
    def __init__(self, ship_list) -> None:
        self.player_name = None
        self.ship = ship_list  # list[ship]
        self.board = None
        self.scan_board = None
        self.player_health = 0

    def __str__(self) -> str:
        return self.player_name

    def player_health_initializer(self, ):
        for ship in self.ship:
            self.player_health += ship.ship_health
        return self.player_health

    def player_health_change(self, ):
        self.player_health -= 1

    def player_info(self, ):
        self.player_name = input("Player 1 please enter your name: ")
        print("{}'s Placement Board".format(self.player_name))

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
