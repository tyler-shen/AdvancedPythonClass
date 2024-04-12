class Game2048:
    def __init__(self, size: int = 4):
        self.board = [[0 for _ in range(size)] for _ in range(size)]

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


game = Game2048()
game.display()
