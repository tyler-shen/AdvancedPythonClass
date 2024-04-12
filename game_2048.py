import random
from typing import List
from copy import deepcopy
from msvcrt import getch


class Game2048:
    def __init__(self, size: int = 4):
        self.board = [[0 for _ in range(size)] for _ in range(size)]
        for _ in range(2):
            self.random_tile()

    def random_tile(self):
        if self.is_board_full():
            return

        random_init_num = random.choice([2, 2, 2, 2, 2, 2, 2, 2, 2, 4])
        while True:
            col_pos = random.randint(0, len(self.board)) - 1
            row_pos = random.randint(0, len(self.board)) - 1
            if self.board[row_pos][col_pos] == 0:
                self.board[row_pos][col_pos] = random_init_num
                break

    def is_board_full(self):
        for row in self.board:
            if 0 in row:
                return False
        return True

    def is_game_over(self):
        game_over = False
        # check if the board is full (game is not over when there is empty space on the board)
        if self.is_board_full():
            # backup the original board
            original_board = deepcopy(self.board)

            # test if there is an action has affects
            game_over = True
            if self.move_left():
                game_over = False
            elif self.move_right():
                game_over = False
            elif self.move_up():
                game_over = False
            elif self.move_down():
                game_over = False

            # restore the original board
            self.board = original_board

        return game_over

    def collapse(self, tiles: List[int]):
        # Preparation
        pos1, pos2 = None, None
        output = []

        # Iterate each tile
        for tile in tiles:
            # Skip if the tile is empty (when tile == 0)
            if tile == 0:
                continue
            pos2 = tile

            # Can they merge?
            if (
                pos1 is None or pos2 is None
                or pos1 == 0 or pos2 == 0
                or pos1 != pos2
            ):
                # No merge
                # Erase and store if it's not empty
                if pos1 is not None and pos1 != 0:
                    output.append(pos1)
                # Move value on pos2 to pos1
                pos1 = pos2

            else:
                # Able to merge
                # Addition (combine two tiles)
                output.append(pos1 + pos2)
                # Clear the pos1 and pos2
                pos1, pos2 = None, None

        # Termination
        if pos1 is not None and pos1 != 0:
            output.append(pos1)
        for _ in range(len(output), len(self.board)):
            output.append(0)

        return output

    def move_left(self):
        affected = False
        for row_idx in range(len(self.board)):
            # Take out a row from the game board
            row = self.board[row_idx]

            # Do collapse on the row
            out_row = self.collapse(tiles=row)
            if out_row != row:
                affected = True

            # Put back the row to the game board
            self.board[row_idx] = out_row
        return affected

    def move_right(self):
        affected = False
        for row_idx in range(len(self.board)):
            # Take out a row from the game board
            row = self.board[row_idx]

            # Do collapse on the row, reverse the rows so it's equivalent to move to the right
            row.reverse()
            out_row = self.collapse(tiles=row)
            if out_row != row:
                affected = True
            out_row.reverse()

            # Put back the row to the game board
            self.board[row_idx] = out_row
        return affected

    def move_up(self):
        affected = False
        for col_idx in range(len(self.board)):
            # Take out a column from the game board
            col = []
            for row_idx in range(len(self.board)):
                row = self.board[row_idx]
                col_val = row[col_idx]
                col.append(col_val)

            # Do collapse on the column
            out_col = self.collapse(tiles=col)
            if out_col != col:
                affected = True

            # Put back the column to the game board
            for row_idx in range(len(self.board)):
                self.board[row_idx][col_idx] = out_col[row_idx]
        return affected

    def move_down(self):
        affected = False
        for col_idx in range(len(self.board)):
            # Take out a column from the game board
            col = []
            for row_idx in range(len(self.board)):
                row = self.board[row_idx]
                col_val = row[col_idx]
                col.append(col_val)

            # Do collapse on the column
            col.reverse()
            out_col = self.collapse(tiles=col)
            if out_col != col:
                affected = True
            out_col.reverse()

            # Put back the column to the game board
            for row_idx in range(len(self.board)):
                self.board[row_idx][col_idx] = out_col[row_idx]
        return affected

    def display(self):
        print(f"+ --- " * len(self.board), end="")
        print(f"+")

        for row_i in range(len(self.board)):
            for col_i in range(len(self.board)):
                print(f"|", end="")
                cell_value = self.board[row_i][col_i]
                if cell_value == 0:
                    print(f" " * 5, end="")
                else:
                    print(f"{cell_value:^5d}", end="")
            print(f"|")
            print(f"+ --- " * len(self.board), end="")
            print(f"+")


if __name__ == "__main__":
    game = Game2048()
    game.display()

    while not game.is_game_over():
        # Grab user input (action)
        # user_action = input("Enter w(up), s(down), a(left), d(right) > ")
        print("Enter w(up), s(down), a(left), d(right) > ")
        user_action = input()
        print(f"{user_action=}")

        # Execute the action on the game board
        if user_action == "w":
            board_changed = game.move_up()
        elif user_action == "s":
            board_changed = game.move_down()
        elif user_action == "a":
            board_changed = game.move_left()
        elif user_action == "d":
            board_changed = game.move_right()
        else:
            print("Invalid input!")
            continue

        # Randomly generate a new tile if the game board been changed
        # and there is empty cell on the board
        if board_changed:
            game.random_tile()

            game.display()

    print("Game Over!")
