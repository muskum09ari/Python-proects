from datetime import date
import tkinter as tk


today = date.today()
 
#function
def get_age():
    d= int(e1.get())
    m=int(e2.get())
    y=int(e3.get())
    age =today.year-y-((today.month, today.day)<(m,d))
    t1.config(state='normal')
    t1.delete('1.0', tk.END)
    t1.insert(tk.END,age)
    t1.config(state='disabled')
 

root = tk.Tk()
root.geometry("500x300")
root.config(bg="cyan")
root.resizable(width=False,height=False)
root.title('Age Calculator')
 
l1 = tk.Label(root,text="Age Calculator:",font=("Arial", 20),fg="blue").place(x=70,y=5)
l_d=tk.Label(root,text="Date: ",font=('Arial',12,"bold"),fg="purple").place(x=100,y=70)
l_m=tk.Label(root,text="Month: ",font=('Arial',12,"bold"),fg="purple").place(x=100,y=95)
l_y=tk.Label(root,text="Year: ",font=('Arial',12,"bold"),fg="purple").place(x=100,y=120)

e1=tk.Entry(root,width=5).place(x=180,y=70)
e2=tk.Entry(root,width=5).place(x=180,y=95)
e3=tk.Entry(root,width=5).place(x=180,y=120)
 
b1=tk.Button(root,text="Calculate Age",font=("Arial",13),command=get_age,bg="orange").place(x=100,y=150)
 
l3 = tk.Label(root,font=('Arial',12,"bold"),fg="cyan").place(x=50,y=200)

t1=tk.Text(root,width=10,height=0,state="disabled").place(x=135,y=203)
 


root.mainloop()