"""
This File:
    
"""


class Player(object):
    def __init__(self) -> None:
        self.name = None
        self.piece = None

    def __str__(self) -> str:
        return self.name

