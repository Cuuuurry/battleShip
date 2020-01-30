"""
This File:
    Player information:
        player name

"""
import sys
import typing


class Player(object):
    def __init__(self) -> None:
        self.name = None
        self.ps_load_ship = None

    def __str__(self) -> str:
        return self.name

    def initial_info(self, ):
        self.name = input("Player 1 please enter your name: ")
        print("{}'s Placement Board".format(self.name))
        return self.name

    def process_info(self):
        self.ps_load_ship = input("{} ".format(self.name, ))

Bob enter horizontal or vertical for the orientation of Patrol which is 2 long: Bob, enter the starting position for your Patrol ship ,which is 2 long, in the form row, column: Bob's Placement Board
Bob enter horizontal or vertical for the orientation of Submarine which is 3 long: Bob, enter the starting position for your Submarine ship ,which is 3 long, in the form row, column: Bob's Placement Board


