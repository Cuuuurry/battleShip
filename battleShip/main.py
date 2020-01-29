#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
This File:
    Main script for Battleship game execution
"""


import sys
from player import Player
from sys import argv

if __name__ == '__main__':
    # get line information in the configs file
    ship_size_dict = {}
    board_size = []
    with open(argv[1], "r") as f:
        for i, line in enumerate(f):
            if i == 0:
                board_size = [int(size) for size in line.split()]
            else:
                ship_size_dict[line.split()[0]] = line.split()[1]

    # call player class
    test = Player()
    test.initial_info()

    """
    board_dim = 3
    for pos, val in enumerate(sys.argv):
        print(f'{pos}: {val}')
    if len(sys.argv) >= 2:  # user provided a board dimension
        # board_dim = int(sys.argv[1])
        pass
    # game = TicTacToeGame(board_dim)
    # game.play()
    """