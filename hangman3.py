import tkinter as tk
from tkinter import messagebox
from string import ascii_uppercase
import random

window = tk.Tk()
window.title('Hangman-Game')

# Change the icon image path to the correct one
window.iconphoto(False, tk.PhotoImage(file="images/icon.png"))

background_image = tk.PhotoImage(file="images/background (2).png")

def display_start_image():
    start_image = tk.PhotoImage(file="images/hang00.png")
    start_label = tk.Label(window, image=start_image)
    start_label.image = start_image  # Keep a reference to avoid garbage collection
    start_label.grid(row=0, column=0, columnspan=10, padx=10, pady=10)

display_start_image()

word_list = ['MUMBAI','DELHI','BANGLORE','HYDRABAD','AHMEDABAD','CHENNAI','KOLKATA','SURAT','PUNE','JAIPUR','AMRITSAR','ALLAHABAD','RANCHI',
            'LUCKNOW','KANPUR','NAGPUR','INDORE','THANE','BHOPAL','PATNA','GHAZIABAD','AGRA','FARIDABAD','MEERUT','RAJKOT','VARANASI','SRINAGAR',
            'RAIPUR','KOTA','JHANSI']

photos = [tk.PhotoImage(file="images/hang0.png"), tk.PhotoImage(file="images/hang1.png"), tk.PhotoImage(file="images/hang2.png"),
          tk.PhotoImage(file="images/hang3.png"), tk.PhotoImage(file="images/hang4.png"), tk.PhotoImage(file="images/hang5.png"),
          tk.PhotoImage(file="images/hang6.png"), tk.PhotoImage(file="images/hang7.png")]


def newGame():
    global the_word_withSpaces
    global numberOfGuesses
    global score
    score = 0
    numberOfGuesses = 0
    
    the_word = random.choice(word_list)
    the_word_withSpaces = " ".join(the_word)
    lblWord.set(' '.join("_" * len(the_word)))
   
def guess(letter):
    global numberOfGuesses
    if numberOfGuesses < 7:
        txt = list(the_word_withSpaces)
        guessed = list(lblWord.get())
        if the_word_withSpaces.count(letter) > 0:
            for c in range(len(txt)):
                if txt[c] == letter:
                    guessed[c] = letter
                lblWord.set("".join(guessed))
                if lblWord.get() == the_word_withSpaces:
                    messagebox.showinfo("Hangman", "You guessed it!")
            # Disable the button once guessed correctly
            button_index = ascii_uppercase.index(letter)
            button_list[button_index].config(state="disabled")
        else:
            numberOfGuesses += 1
            imgLabel.config(image=photos[numberOfGuesses])
            if numberOfGuesses == 7:
                messagebox.showwarning("Hangman", "Game Over")
            # Disable the button once guessed incorrectly
            button_index = ascii_uppercase.index(letter)
            button_list[button_index].config(state="disabled")

imgLabel = tk.Label(window, image=background_image)
imgLabel.place(x=0, y=0, relwidth=1, relheight=1)

imgLabel = tk.Label(window)
imgLabel.grid(row=0, column=0, columnspan=3, padx=10, pady=40)

lblWord = tk.StringVar()
tk.Label(window, textvariable=lblWord, font=('consolas 24 bold')).grid(row=0, column=3, columnspan=6, padx=10)
canvas = tk.Canvas(window, width=1000,height=300)
canvas.grid(row=1, column=0, columnspan=10, padx=10, pady=10)

button_frame = tk.Frame(window)
button_frame.grid(row=1, column=0, columnspan=10, padx=10, pady=10)

button_list = []

for index, char in enumerate("ABCDEFGHIJKLMNOPQRSTUVWXYZ"):
    row, col = divmod(index, 6)
    button = tk.Button(button_frame, text=char, font=("Helvetica", 12), width=4, bg="aqua", command=lambda ch=char: guess(ch))
    button.grid(row=row, column=col, padx=5, pady=5)
    button_list.append(button)

newGame()

new_game_button = tk.Button(window, text="New Game", command=newGame, font=("Helvetica", 12, "bold"))
new_game_button.grid(row=2, column=0, columnspan=10, pady=10)

window.mainloop()
