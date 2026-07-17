import tkinter as tk
from tkinter import messagebox
import random
import os

def load_words():
    """Reads words from words.txt"""
    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_dir, "words.txt")
    if os.path.exists(file_path):
        try:
            with open(file_path, "r") as file:
            #Reads lines, strip out hidden spaces and skip empty lines, if any
                words = [line.strip().upper() for line in file if line.strip()]
                return words
        except Exception:
            print("Text file missing or corrupt")
            return []
    else:
        print(f"Looking for file at: {file_path} - But it was not found")
        return [] 

WORD_LIST = load_words()



class HangmanGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Hangman game")
        self.root.geometry("800x650")
        self.root.configure(bg="#2C3E50")

        #Game state variables
        self.guessed_letters = set()
        self.max_attempts = 6
        self.wrong_attempts = 0

        if WORD_LIST:
            self.word = random.choice(WORD_LIST)
        else:
            self.word = "DEFAULT"

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
        self.draw_hangman()


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
    def draw_hangman(self):
        """Draws the hangman parts based on wrong attempts."""
        self.canvas.delete("all")# clears canvas old shapes and new shapes mixing together

        # colors for diagrams(wooden gallows and the rope)
        wood_color = "#E67E22"
        rope_color = "#f1c40f"
        skin_color = "#ecf0f1"

        #Diagram of the gallows = self.canvas.create_line (x1,y1,x2,y2,...)
        self.canvas.create_line(20,180,100,180, fill=wood_color, width=4)#Base
        self.canvas.create_line(60,180,60,20, fill=wood_color, width=4)#Post
        self.canvas.create_line(60,20,160,20, fill=wood_color,width=4)#Beam
        self.canvas.create_line(160,20,160,50, fill=rope_color, width=3)#Rope

        #Drawing stick figure step-by-step based on wrong attempts
        if self.wrong_attempts >=1:
            #1. Head(creates oval)
            self.canvas.create_oval(145,50,175,80, outline=skin_color, width=3)

        if self.wrong_attempts >=2:
            #2. Body(Line from neck to hips)
            self.canvas.create_line(160,80,160,130, fill=skin_color, width=3)

        if self.wrong_attempts >=3:
            #3. Left arm(diagonal line)
            self.canvas.create_line(160,95,140,115, fill=skin_color, width=3)
        
        if self.wrong_attempts >=4:
            #4. right arm
            self.canvas.create_line(160,95,180,115, fill=skin_color, width=3)

        if self.wrong_attempts >=5:
            #5. Left leg
            self.canvas.create_line(160,130,140,165, fill=skin_color, width=3)

        if self.wrong_attempts >=6:
            #6. Right leg
            self.canvas.create_line(160,130,180,165, fill=skin_color, width=3)


    def guess_letter(self, letter):
        """Processes a player's letter guess."""
        self.guessed_letters.add(letter)

        #Finds the clicked button and disable it
        for child in self.keyboard_frame.winfo_children():
            if child.cget("text") == letter:
                child.config(state="disabled", bg="#7f8c8d")

        if letter in self.word:
            self.word_label.config(text=self.get_display_word())
            if "_" not in self.get_display_word():
                messagebox.showinfo("Victory!", f"You won! The word was {self.word}")
                self.reset_game()
        else:
            self.wrong_attempts +=1
            self.draw_hangman()

            if self.wrong_attempts >= self.max_attempts:
                messagebox.showerror("Game Over", f"You ran out of attempts! The word was {self.word}")
                self.reset_game()
            

    def reset_game(self):
        """Resets the state to start a new game."""
        self.guessed_letters = set()
        self.wrong_attempts = 0
        if WORD_LIST:
            self.word = random.choice(WORD_LIST).upper()
        else:
            self.word = "DEFAULT"
        self.word_label.config(text=self.get_display_word())
        self.create_keyboard()
        self.draw_hangman()

        
if __name__ == "__main__":
    root = tk.Tk()
    app = HangmanGUI(root)
    root.mainloop()   
    