import tkinter as tk
from tkinter import messagebox

class TTTBoard:
    def __init__(self):
        self.board = [""] * 9
        self.current_player = "X"
        self.winner = None
        self.game_over = False

    def make_move(self, idx):
        if self.board[idx] == "" and not self.game_over:
            self.board[idx] = self.current_player
            self.check_winner()
            if not self.game_over:
                self.current_player = "O" if self.current_player == "X" else "X"
            return True
        return False

    def check_winner(self):
        win_conditions = [
            (0,1,2), (3,4,5), (6,7,8),  # Rows
            (0,3,6), (1,4,7), (2,5,8),  # Columns
            (0,4,8), (2,4,6)            # Diagonals
        ]
        for i, j, k in win_conditions:
            if self.board[i] == self.board[j] == self.board[k] != "":
                self.winner = self.board[i]
                self.game_over = True
                return

        if "" not in self.board:
            self.winner = "Hòa"
            self.game_over = True

    def reset(self):
        self.__init__()

class TTTApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic-Tac-Toe")
        self.board = TTTBoard()
        self.buttons = []
        self.create_widgets()

    def create_widgets(self):
        for i in range(9):
            btn = tk.Button(self.root, text="", font=("Arial", 32), width=5, height=2,
                            command=lambda i=i: self.handle_click(i))
            btn.grid(row=i//3, column=i%3)
            self.buttons.append(btn)

        self.status_label = tk.Label(self.root, text="Lượt: X", font=("Arial", 16))
        self.status_label.grid(row=3, column=0, columnspan=3, pady=10)

        self.reset_button = tk.Button(self.root, text="Chơi lại", font=("Arial", 12), command=self.reset_game)
        self.reset_button.grid(row=4, column=0, columnspan=3)

    def handle_click(self, idx):
        if self.board.make_move(idx):
            self.buttons[idx].config(text=self.board.board[idx], state="disabled")
            if self.board.game_over:
                if self.board.winner == "Hòa":
                    self.status_label.config(text="Hòa!")
                    messagebox.showinfo("Kết quả", "Hòa!")
                else:
                    self.status_label.config(text=f"{self.board.winner} thắng!")
                    messagebox.showinfo("Kết quả", f"{self.board.winner} thắng!")
                for btn in self.buttons:
                    btn.config(state="disabled")
            else:
                self.status_label.config(text=f"Lượt: {self.board.current_player}")

    def reset_game(self):
        self.board.reset()
        for btn in self.buttons:
            btn.config(text="", state="normal")
        self.status_label.config(text="Lượt: X")

if __name__ == "__main__":
    root = tk.Tk()
    app = TTTApp(root)
    root.mainloop()