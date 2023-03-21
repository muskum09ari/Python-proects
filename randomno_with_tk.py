
from tkinter import * 
import tkinter as tk
import random

window = tk.Tk()
window.title("Number Guessing Game")
window.geometry("500x400")
window.config(bg = "pink")
window.resizable(width = False, height = False)

heading = Label(window,text = 'Lets play Number Guessing',font = 'arial',bg = 'cyan',fg = 'black').place(x=100,y=50)
  

number = random.randint(1, 100)

def check_guess():
    guess = int(guess_entry.get())
    if guess == number:
        result_label.config(text="Congratulations! You guessed the number.",fg="dark blue")
    elif guess > number:
        result_label.config(text="Too high. Try again.",fg="dark blue")
    else:
        result_label.config(text="Too low. Try again.",fg="dark blue")

instructions_label = tk.Label(window, text="Guess a number between 1 and 100:")
instructions_label.place(x=170,y=170)

guess_entry = tk.Entry(window)
guess_entry.place(x=170,y=200)

guess_button = tk.Button(window, text="Guess",bg="yellow", command=check_guess)
guess_button.place(x=200,y=230)

result_label = tk.Label(window, text="")
result_label.place(x=180,y=260)

window.mainloop()

