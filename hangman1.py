import tkinter as tk
from tkinter import messagebox
from string import ascii_uppercase
import random

window = tk.Tk()
window.title('Hangman-Game')


background_image = tk.PhotoImage(file="images/background.png")

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
                button_index = ascii_uppercase.index(letter)
                canvas.itemconfig(button_list[button_index], fill="lightgreen")    
        else:
            numberOfGuesses += 1
            imgLabel.config(image=photos[numberOfGuesses])
            if numberOfGuesses == 7:
                messagebox.showwarning("Hangman", "Game Over")
            
            button_index = ascii_uppercase.index(letter)
            canvas.itemconfig(button_list[button_index], fill="red")

imgLabel = tk.Label(window, image=background_image)
imgLabel.place(x=0, y=0, relwidth=1, relheight=1)

imgLabel = tk.Label(window)
imgLabel.grid(row=0, column=0, columnspan=3, padx=10, pady=40)

lblWord = tk.StringVar()
tk.Label(window, textvariable=lblWord, font=('consolas 24 bold')).grid(row=0, column=3, columnspan=6, padx=10)
canvas = tk.Canvas(window, width=1000,height=300)
canvas.grid(row=1, column=0, columnspan=10, padx=10, pady=10)



# Create a canvas for the round buttons
button_radius = 20
button_spacing = 50
button_start_x = 25
button_start_y = 25

button_list = []

n = 0
for c in ascii_uppercase:
    x = button_start_x + (n % 6) * button_spacing
    y = button_start_y + (n // 6) * button_spacing
    button = canvas.create_oval(x - button_radius, y - button_radius, x + button_radius, y + button_radius, fill="aqua", outline="black")
    canvas.create_text(x, y, text=c, font=("Helvetica", 12))
    canvas.tag_bind(button, "<Button-1>", lambda event, char=c: guess(char))
    button_list.append(button)
    n += 1

# Define buttons on the right side of the window
right_button_frame = tk.Frame(window)
right_button_frame.grid(row=1, column=9, rowspan=3, padx=10, pady=10)

def create_button(char):
    return tk.Button( right_button_frame,text=char, command=lambda: guess(char), font=('Helvetica 18'), bg="aqua", width=4)

for char in ascii_uppercase[26:30]:
    button = create_button(char)
    button.pack(side=tk.TOP)

tk.Button(window, text="New\nGame", command=newGame,font=("Helvetica 10 bold")).grid(row=3, column=8)

newGame()
window.mainloop()
