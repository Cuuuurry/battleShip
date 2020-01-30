"""
This File:
    Printout game information for players
"""
import sys
import typing


class Player(object):
    def __init__(self) -> None:
        self.player_name = None
        self.ship = ship_list  # list[ship]
        self.board = None
        self.scan_board = None

    def __str__(self) -> str:
        return self.player_name

    def player_info(self, ):
        self.player_name = input("Player 1 please enter your name: ")
        print("{}'s Placement Board".format(self.player_name))
        return self.player_name

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

    def fire_on_target(self, ):
        print("You hit {}'s {}!".format(self.player_name, self.ship_name))

    def ship_status(self, ):
        print("You destroyed {}'s {}".format(self.player_name, self.ship_name))

    def game_result(self, ):
        print("{} won the game!".format(self.player_name))
