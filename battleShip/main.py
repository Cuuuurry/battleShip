#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
This File:
    Main script for Battleship game execution
"""

from sys import argv
from battleship import BattleShip
import numpy as np

if __name__ == '__main__':
    # get line information in the configs file
    seed_number = argv[2]
    np.random.seed(int(seed_number))
    ship_size_dict = {}
    board_size = []
    with open(argv[1], "r") as f:
        for i, line in enumerate(f):
            if i == 0:
                board_size = [int(size) for size in line.split()]
            else:
                ship_size_dict[line.split()[0]] = line.split()[1]

    test = BattleShip(board_size[0], board_size[1], ship_size_dict)
    test.play()
