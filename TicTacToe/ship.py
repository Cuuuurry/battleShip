"""
This File:
    Ship information
"""

import typing

class ship(object):
    def __init__(self, shipNum: int):
        self.shipNum = shipNum
        self.ship_dict = {}

    def ship_num_setup(self):
        for i in range(self.shipNum):
            newitem = input("Please enter the new ship name")
            if newitem in self.ship_dict:
                raise Exception("The category of ship have existed")
                erase = input("The category of ship have existed. \n"
                              "Do you want to redefine the number of item? \n  "
                              "Enter True or False.")
                if erase == "True" or "true":
                    newnum = input("Please enter the new numbers of ships")
            else:
                newnum = input("Please enter the new numbers of ships")
            self.ship_dict[newitem] = {}
            self.ship_dict[newitem]["num"] = int(newnum)

    def ship_size_setup(self):
        for i in range(self.shipNum):
            newitem = input("Please enter the new ship name")
            if newitem in self.ship_dict:
                raise Exception("The category of ship have existed")
                erase = input("The category of ship have existed. \n"
                              "Do you want to redefine the number of item? \n  "
                              "Enter True or False.")
                if erase == "True" or "true":
                    newnum = input("Please enter the new numbers of ships")
            else:
                newnum = input("Please enter the new numbers of ships")
            self.ship_dict[newitem] = {}
            self.ship_dict[newitem]["num"] = int(newnum)

