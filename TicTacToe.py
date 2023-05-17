from tkinter import messagebox
import tkinter as tk

class TicTacToe:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Tic Tac Toe")
        self.window.geometry("200x400")

        self.moves = [""] * 9  # Track the moves made on the board
        self.current_player = "X"  # Player X starts the game
        self.move_count = 0  # Total moves made in the game

        self.buttons = []
        for i in range(9):
            button = tk.Button(
                self.window,
                width=8,
                height=8,
                text=str(i + 1),
                fg="blue",
                bg="blue",
                command=lambda i=i: self.make_move(i),
            )
            button.grid(row=i // 3, column=i % 3)
            self.buttons.append(button)

    def make_move(self, index):
        if self.moves[index] == "":
            self.moves[index] = self.current_player
            self.buttons[index].config(text=self.current_player, fg="white")
            self.move_count += 1

            if self.check_winner():
                messagebox.showinfo("Game Over", f"Player {self.current_player} wins!")
                self.reset_game()
            elif self.move_count == 9:
                messagebox.showinfo("Game Over", "It's a draw!")
                self.reset_game()
            else:
                self.current_player = "O" if self.current_player == "X" else "X"

    def check_winner(self):
        winning_combinations = (
            (0, 1, 2),
            (3, 4, 5),
            (6, 7, 8),
            (0, 3, 6),
            (1, 4, 7),
            (2, 5, 8),
            (0, 4, 8),
            (2, 4, 6),
        )

        for combination in winning_combinations:
            a, b, c = combination
            if (
                self.moves[a]
                and self.moves[a] == self.moves[b]
                and self.moves[b] == self.moves[c]
            ):
                return True

        return False

    def reset_game(self):
        self.moves = [""] * 9
        self.current_player = "X"
        self.move_count = 0

        for button in self.buttons:
            button.config(text="", fg="blue")

    def run(self):
        self.window.mainloop()

game = TicTacToe()
game.run()
