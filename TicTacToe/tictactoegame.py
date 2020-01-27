class TicTacToeGame(object):
    def __init__(self, dimensions: int) -> None:
        self.board = None
        self.players = [None] * 2
        self._cur_player_turn = 0

    def play(self) -> None:
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

    def someone_won_vertically(self) -> bool:
        for col in zip(*self.board):
            if all_same(col):
                return True
        else:
            return False

    def someone_won_diagonally(self) -> bool:
        return self.someone_won_with_left_diagonal() or self.someone_won_with_right_diagonal()

    def someone_won_with_left_diagonal(self) -> bool:
        """
        Someone won like this
        X
          X
            X
        :return:
        """
        return all_same((self.board[i][i] for i in range(self.board.num_rows)))

    def someone_won_with_right_diagonal(self) -> bool:
        """
        Some won like
            X
          X
        X
        :return:
        """

    def tie_game(self) -> bool:
        """
        This should only be called after a check for a win is done
        :return:
        """
        return self.board.is_full()

    def change_turn(self) -> None:
        self._cur_player_turn = (self._cur_player_turn + 1) % 2
        # if self._cur_player_turn == 0:
        #     self._cur_player_turn = 1
        # else:
        #     self._cur_player_turn = 0

    def get_cur_player(self) -> "Player":
        return self.players[self._cur_player_turn]
