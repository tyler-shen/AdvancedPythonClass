import random

class Game2048:
    def __init__(self, size: int = 4):
        self.board = [[0 for _ in range(size)] for _ in range(size)]
        for _ in range(2):
            # self.random_tile()
            self.board[0][0] = 2
            self.board[0][1] = 2

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

    def random_tile(self):
        random_init_num = random.choice([2, 2, 2, 2, 2, 2, 2, 2, 2, 4])
        while True:
            col_pos = random.randint(0, len(self.board)) - 1
            row_pos = random.randint(0, len(self.board)) - 1
            if self.board[row_pos][col_pos] == 0:
                self.board[row_pos][col_pos] = random_init_num
                break

    def move_left(self):
        for row_idx in range(len(self.board)):
            # Take out a row from the game board
            row = self.board[row_idx]

            # Do collapse on the row
            out_row = self.collapse(tiles=row)

            # Put back the row to the game board
            self.board[row_idx] = out_row

    def collapse(self, tiles):
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

    def move_right(self):
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

    def move_up(self):
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

    def move_down(self):
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


game = Game2048()
game.display()

user_action = input("Enter w(up), s(down), a(left), d(right) > ")
if user_action == "w":
    game.move_up()
elif user_action == "s":
    game.move_down()
elif user_action == "a":
    game.move_left()
elif user_action == "d":
    game.move_right()
else:
    print("Invalid input!")

game.display()
