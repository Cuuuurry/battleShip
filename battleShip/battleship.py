"""
This File:
    Class battleShip for game process

"""

from typing import Iterable, TypeVar
from board import Board
from player import Player
from ship import Ship
print("Successfully import classes")


class BattleShip(object):
    """
    Summary:
        Two players
        Four boards: two initial boards (static), two scan boards (dynamic)
    """
    def __init__(self, num_rows: int, num_cols: int, is_scan: bool = False, miss_char: str = "X",
                 aim_char: str = "O") -> None:
        self.blank_char = blank_char
        self.board = Board(num_rows, num_cols, is_scan)
        self.players = [Player() for _ in range(2)]
        self.cur_player_turn = 0

    def play(self) -> None:
        """
        Summary:
                Main loop of the game

        :return:
        """
        while not self.is_game_over():
            self.display_game_state()
            cur_player = self.get_cur_player()
            the_move = cur_player.get_move()
            the_move.make()
            self.change_turn()
        self.display_the_winner()

    def display_game_state(self) -> None:
        print(self.board)

    def is_game_over(self):
        return self.someone_won() or self.tie_game()

    def someone_won(self) -> bool:
        """

        :return:
        """

        return self.someone_won_horizontally() or self.someone_won_vertically() or self.someone_won_diagonally()

    def someone_won_horizontally(self) -> bool:
        for row in self.board:
            if all_same(row):
                return True
            else:
                return False

        # for i in range(self.board.rows):
        #     if self.board.row_all_same(self.board[i])
        #
        # do any of the rows
        # have all of the same characters
        return any(
            (all_same(row) for row in self.board)
        )

    # a b c
    # d e f
    # h i j



    def change_turn(self):
        self._cur_player_turn = (self._cur_player_turn + 1) % 2
        if self._cur_player_turn == 0:
            self._cur_player_turn = 1
        else:
            self._cur_player_turn = 0

    def get_cur_player(self):

        return self.players[self._cur_player_turn]