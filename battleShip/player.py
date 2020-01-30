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

    def __str__(self) -> str:
        return self.name

    def initial_info(self, ):
        self.name = input("Player 1 please enter your name: ")
        print("{}'s Placement Board".format(self.name))
        return self.name


