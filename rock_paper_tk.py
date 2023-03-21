 
from tkinter import *  
import random  
  
root = Tk()  
root.title("Rock Paper Scissors Game")  
root.geometry("500x400")  
root.config(bg = "light pink")  
root.resizable(width = False, height = False)  
  

heading = Label(root,text ='Rock Paper Scissors',font = 'arial',bg = 'purple',fg = 'white').pack()  
  

userInput = StringVar()  
  
subHeading = Label(root,text = 'Select rock, paper or scissors',font = 'calibri',bg = 'cyan').place(x = 100,y = 110)  
  
Entry(root,font = 'calibri',textvariable = userInput,bg = 'yellow').place(x = 110,y = 160)  
  
  
cs = random.randint(1, 3)  
  
if cs == 1:  
    cs = 'rock'  
elif cs == 2:  
    cs = 'paper'  
else:  
    cs = 'scissors'  
  
 
res = StringVar()  
  
def letsPlay():  
    userSelection = userInput.get()  
    if userSelection == cs:  
        res.set("game tie")  
    elif userSelection == 'rock' and cs == 'paper':  
        res.set("You Lose,Computer chooses paper")  
    elif userSelection == 'rock' and cs == 'scissors':  
        res.set("you win,Computer chooses scissors")  
    elif userSelection == 'paper' and cs == 'scissors':  
        res.set("You Lose,computer chooses scissors")  
    elif userSelection == 'paper' and cs == 'rock':  
        res.set("You Win,computer chooses rock")  
    elif userSelection == 'scissors' and cs == 'rock':  
        res.set("You Lose,computer chooses rock")  
    elif userSelection == 'scissors' and cs == 'paper':  
        res.set("You Win,computer chooses paper")  
    else:  
        res.set("invalid input!")  
  

def resetGame():  
    res.set("")  
    userInput.set("")  
  
  
displayResult = Label(root,textvariable = res,font = 'calibri',bg = 'orange').place(x = 20,y = 240)  
  
playButton = Button(root,font = 'calibri',text = 'PLAY',padx = 5,bg = 'olive',command = letsPlay).place(x = 100,y = 300)  
  
resetButton = Button(root,font = 'calibri',text = 'RESET',padx = 5,bg = 'green',command = resetGame).place(x = 350,y = 300)  
  
  
root.mainloop()  