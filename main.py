import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic-Tac-Toe")
        self.root.geometry("400x450")
        self.root.configure(bg='#2c3e50')

        self.board = [['' for _ in range(3)] for _ in range(3)]
        self.current_player = 'X'
        self.game_over = False

        self.buttons = [[None for _ in range(3)] for _ in range(3)]
        self.create_widgets()

    def create_widgets(self):
        # Title
        title = tk.Label(self.root, text="Tic-Tac-Toe", font=('Arial', 24, 'bold'), bg='#2c3e50', fg='white')
        title.pack(pady=10)

        # Game board frame
        board_frame = tk.Frame(self.root, bg='#34495e')
        board_frame.pack(pady=20)

        for i in range(3):
            for j in range(3):
                self.buttons[i][j] = tk.Button(board_frame, text='', font=('Arial', 40, 'bold'),
                                               width=5, height=2, bg='#ecf0f1', fg='#2c3e50',
                                               command=lambda row=i, col=j: self.on_click(row, col))
                self.buttons[i][j].grid(row=i, column=j, padx=5, pady=5)

        # Restart button
        restart_btn = tk.Button(self.root, text="Restart", font=('Arial', 14), bg='#e74c3c', fg='white',
                                command=self.restart_game)
        restart_btn.pack(pady=10)

        # Status label
        self.status_label = tk.Label(self.root, text="Player X's turn", font=('Arial', 16), bg='#2c3e50', fg='white')
        self.status_label.pack(pady=10)

    def on_click(self, row, col):
        if self.game_over or self.board[row][col] != '':
            return

        self.board[row][col] = self.current_player
        self.buttons[row][col].config(text=self.current_player, fg='#e74c3c' if self.current_player == 'X' else '#3498db')

        if self.check_winner(self.current_player):
            self.status_label.config(text=f"Player {self.current_player} wins!")
            self.game_over = True
            messagebox.showinfo("Game Over", f"Player {self.current_player} wins!")
        elif self.is_board_full():
            self.status_label.config(text="It's a draw!")
            self.game_over = True
            messagebox.showinfo("Game Over", "It's a draw!")
        else:
            self.current_player = 'O' if self.current_player == 'X' else 'X'
            self.status_label.config(text=f"Player {self.current_player}'s turn")

    def check_winner(self, player):
        # Check rows
        for row in self.board:
            if all(cell == player for cell in row):
                return True
        # Check columns
        for col in range(3):
            if all(self.board[row][col] == player for row in range(3)):
                return True
        # Check diagonals
        if all(self.board[i][i] == player for i in range(3)) or all(self.board[i][2-i] == player for i in range(3)):
            return True
        return False

    def is_board_full(self):
        return all(all(cell != '' for cell in row) for row in self.board)

    def restart_game(self):
        self.board = [['' for _ in range(3)] for _ in range(3)]
        self.current_player = 'X'
        self.game_over = False
        self.status_label.config(text="Player X's turn")
        for i in range(3):
            for j in range(3):
                self.buttons[i][j].config(text='', bg='#ecf0f1')

if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()

print("Tic-Tac-Toe game has ended.")
print("Thank you for playing!")