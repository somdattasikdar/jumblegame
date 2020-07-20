import tkinter
from tkinter import *
import random
from tkinter import messagebox


words= [
   "ptonhy",
   "vjaa",
   "ecdo",
   "eorr",
   "etrmocup",
   "meymro",
   "mro",
   "amr",
   "beyt",
   "lptpoa"
]

answers=[
"python",
"java",
"code",
"error",
"computer",
"memory",
"rom",
"ram",
"byte",
"laptop"
]

num = random.randrange(0,10,1)

def res():
    global words,answers,num
    num = random.randrange(0,10,1)
    lbl.config (text = words[num])
    e1.delete(0,END)


def default():
    global words,answers,num
    lbl.config(text = words[num])

def checkans():
    global words,answers,num
    var = e1.get()
    if var == answers[num]:
        messagebox.showinfo("succesfull!","this is the correct answer!!")
        res()
    else:
        messagebox.showerror("not succesfull!")
        e1.delete(0,END)

root =tkinter.Tk()
root.title("jumble word game")
root.geometry("400x400+300+300")
root.configure(background="#000000")

lbl=Label(
    root,
    text = "your text" ,
    font = ("verdana",20),
    bg = "#000000",
    fg = "#FFBF00",
)
lbl.pack(pady=40)

ans1 = StringVar()

e1=Entry(
root,
font = ("verdana",12),
textvar = ans1,
)
e1.pack(ipady=5,ipadx=5)

btncheck = Button(
   root,
   text = "check",
   font = ("comic sans ms",16),
   width = 16,
   bg = "#A52A2A",
   fg = "#800000",
   relief= GROOVE,
   command = checkans,
)
btncheck.pack(pady=40)

btnreset = Button(
   root,
   text = "reset",
   font = ("comis sans ms",16),
   width = 16,
   bg = "#A52A2a",
   fg = "#800000",
   relief= GROOVE,
   command = res,
)
btnreset.pack()
default()

root.mainloop()
