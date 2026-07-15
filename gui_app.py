import tkinter as tk
from tkinter import messagebox
import random

WORD_LIST = ["PYTHON","DEVELOPER","GITHUB", "TERMINAL"]

class HangmanGUI:
    def __init__(self, root):
        self.root = root
        self.root.title(" Python Hangman")
        self.root.geometry("800x650")
        self.root.configure(bg="#2C3E50")

        #Game state variables
        self.word = random.choice(WORD_LIST).upper()
        self.guessed_letters = set()
        self.max_attempts = 6
        self.wrong_attempts = 0

        #Title Label
        self.title_label = tk.Label(
            self.root,
            text = "HANGMAN",
            font =("Helvetica", 24, "bold"),
            bg = "#2C3E50",
            fg = "#ECF0F1"
        )
        self.title_label.pack(pady=10)

        #Canvas for Drawin
        self.canvas = tk.Canvas(
            self.root,
            width = 250,
            height=200,
            bg="#34495E",
            highlightthickness=0
        )
        self.canvas.pack(pady = 10)

        #Dynamic Word Display Label
        self.word_label = tk.Label(
            self.root,
            text= self.get_display_word(),
            font = ("Helvetica", 24, "bold"),
            bg="#2c3e50",
            fg="#1ABC9C"
        )
        self.word_label.pack(pady=15)

        #Frame to hold the A-Z buttons
        self.keyboard_frame = tk.Frame(self.root, bg="#2c3e50")
        self.keyboard_frame.pack(pady = 15)

        self.create_keyboard()


    def get_display_word(self):
        """Returns the secret word with underscores for unguessed letters."""
        return " ".join([letter if letter in self.guessed_letters else "_" for letter in self.word])

    #on-screen keyboard
    def create_keyboard(self):
        """Generate the A-Z on screen keyboard."""
        alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

        #button arrangement in 2 rows of 13
        for i, letter in enumerate(alphabet):
            row = i // 13
            col = i % 13

            btn = tk.Button(
                self.keyboard_frame,
                text=letter,
                font=("Helvetica", 12, "bold"),
                width=4,
                height=2,
                bg="#ecf0f1",
                fg="#2c3e50",
                activebackground= "#1abc9c",

                command = lambda l=letter: self.guess_letter(l)
            )
            btn.grid(row=row, column = col, padx=4, pady=4)

    def guess_letter(self, letter):
        """Processes a player's letter guess."""
        self.guessed_letters.add(letter)

        #Finds the clicked button and disable it
        for child in self.keyboard_frame.winfo_children():
            if child.cget("text") == letter:
                child.config(state="disabled", bg="#7f8c8d")

        #Update the underscore display
        self.word_label.config(text=self.get_display_word())

        
if __name__ == "__main__":
    root = tk.Tk()
    app = HangmanGUI(root)
    root.mainloop()   
    