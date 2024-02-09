class GameOver:

    def __init__(self, cells: list, char: str, player: str):
        self.all_cells = cells
        self.player = player
        self.char = char

    def check_answer(self):
        if self.all_cells[0] == self.char and self.all_cells[1] == self.char and self.all_cells[2] == self.char:
            print(f"Player {self.player} is the winner 🏆")
            return True

        elif self.all_cells[3] == self.char and self.all_cells[4] == self.char and self.all_cells[5] == self.char:
            print(f"Player {self.player} is the winner 🏆")
            return True

        elif self.all_cells[6] == self.char and self.all_cells[7] == self.char and self.all_cells[8] == self.char:
            print(f"Player {self.player} is the winner 🏆")
            return True

        elif self.all_cells[0] == self.char and self.all_cells[3] == self.char and self.all_cells[6] == self.char:
            print(f"Player {self.player} is the winner 🏆")
            return True

        elif self.all_cells[1] == self.char and self.all_cells[4] == self.char and self.all_cells[7] == self.char:
            print(f"Player {self.player} is the winner 🏆")
            return True

        elif self.all_cells[2] == self.char and self.all_cells[5] == self.char and self.all_cells[8] == self.char:
            print(f"Player {self.player} is the winner 🏆")
            return True

        elif self.all_cells[0] == self.char and self.all_cells[4] == self.char and self.all_cells[8] == self.char:
            print(f"Player {self.player} is the winner 🏆")
            return True

        elif self.all_cells[2] == self.char and self.all_cells[4] == self.char and self.all_cells[6] == self.char:
            print(f"Player {self.player} is the winner 🏆")
            return True
