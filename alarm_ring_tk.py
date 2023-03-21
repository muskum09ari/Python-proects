  
from tkinter import *  
import datetime as dt  
import time  
from playsound import playsound
   

def alarm(setAlarmTimer):  
    while True:  
        time.sleep(1)  
        actualTime = dt.datetime.now()  
        currentTime = actualTime.strftime("%H : %M : %S")  
        currentDate = actualTime.strftime("%d / %m / %Y")  
        the_message = "Current Time: " + str(currentTime)  
        print(the_message)  
        if currentTime == setAlarmTimer:  
            playsound('C:\\Users\\HP\\OneDrive\\Desktop\\python Training\\happy-birthday-in-english-male-15023.mp3')  
            break  
  
def getAlarmTime():  
    alarmSetTime = f"{hour.get()} : {minute.get()} : {second.get()}"  
    alarm(alarmSetTime)  
  

root = Tk()  
root.title("Alarm Clock")  
root.geometry("464x200")  
root.config(bg = "cyan")  
root.resizable(width = False, height = False)  
 
   
add_time = Label(  
    root,  
    text = "Hour     Minute     Second",  
    font = 60,  
    fg = "dark red",  
    bg = "light blue"  
    ).place(  
        x = 220,  
        y = 10  
        )  
  
setAlarm = Label(  
    root,  
    text = "Set Time for Alarm: ",  
    fg = "dark blue",  
    bg = "light pink",  
    relief = "solid",  
    font = ("Helevetica", 13, "bold")  
    ).place(  
        x = 5,  
        y = 50  
        )  
   
hour = StringVar()  
minute = StringVar()  
second = StringVar()  
   
hourTime = Entry(  
    root,  
    textvariable = hour,  
    bg = "light pink",  
    width = 4,  
    font = (20)  
    ).place(  
        x = 220,  
        y = 53  
        )  
minuteTime = Entry(  
    root,  
    textvariable = minute,  
    bg = "light pink",  
    width = 4,  
    font = (20)  
    ).place(  
        x = 297,  
        y = 53  
        )  
secondTime = Entry(  
    root,  
    textvariable = second,  
    bg = "light pink",  
    width = 4,  
    font = (20)  
    ).place(  
        x = 390,  
        y = 53  
        )  
   
submit = Button(  
    root,  
    text = "Set The Alarm",  
    fg = "yellow",  
    bg = "blue",  
    width = 15,  
    command = getAlarmTime,  
    font = (20)  
    ).place(  
        x = 140,  
        y = 100  
        )  
   
root.mainloop()  