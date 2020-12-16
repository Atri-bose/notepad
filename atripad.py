from tkinter import *
from tkinter.filedialog import askopenfilename as op
from tkinter.filedialog import asksaveasfilename as sv
import tkinter.messagebox as tmsg
import os
import googlesearch
from urllib.request import urlopen as req
import webbrowser
font = "calibiri "
size = 10
sizestr = str(size)
special = ""
ft = font + sizestr + " " + special
root = Tk()
file = None
f = "Untitled"


def b():
    global special
    special = " bold"
def i():
    global special
    special ="italics"
def u():
    global special
    special ="underline"
def fonti():
    global font
    shoot = Tk()
    shoot.title("font")
    s = StringVar()
    def ec():
        nonlocal s
        s.set(no)

    e = Entry(root, textvar=s)
    e.pack()
    with open("f.txt","r") as nf:
        n =  nf.readlines()
        for no in  n:
            Button(shoot,text = e.get())
    with open("f.txt","a") as nf:
        nf.write(e.get() + "\n")
    shoot.mainloop()
    Button(root,command = s).pack()
def new():
    global file
    global t
    t.delete("1.0", END)
    file = "ex2.txt"


def opennew():
    global file
    global t
    global f
    file = op(defaultextension=".txt", filetypes=[("text documents", "*.txt"), ("All Files", "*.*")])
    f = os.path.basename(file)
    with open(file, "r") as f:
        txt = f.read()
    # tx = t.get("1.0",END)
    # t.replace(t,txt,len(txt))
    t.delete("1.0", END)
    t.insert(END, txt)


def save():
    global file
    if file == None:
        saveas()
    else:
        with open(file, "w")as f:
            f.write(t.get("1.0", END))
def saveas():
    file = sv(defaultextension=".txt", filetypes=[("text documents", "*.txt"), ("All Files", "*.*")])
    save()

def quitGUI():
    global root
    try:
        with open(file, "r") as f:
            txt = f.read()
    except FileNotFoundError:
        txt = ""
    if txt != t.get("1.0", END):
        q = tmsg.askquestion("File not saved", "There is some unsaved changes in your file.Do you want to save it?")
        if q:
            root.destroy()
        else:
            pass
    else:
        root.destroy()


def cut():
    global t
    t.event_generate('<Control-x>')


def copy():
    global t
    t.event_generate('<Control-c>')


def paste():
    global t
    t.event_generate('<Control-v>')


def abm():
    tmsg.showinfo("Credits", "all credits belong to Atri Basu Neogi  and code with harry youtube channel")


def searchi():
    global special
    global sizestr
    global t
    f1 = Tk()
    def ui(event):
        sizestr = str(sizestr2.get())
        t.config(font="calibiri" + sizestr)
    sizestr2 = Scale(f1,from_=1,to=100,command = ui)
    sizestr2.pack()
    Button(f1,text="Done",command=f1.destroy).pack()
    f1.mainloop()

root.geometry("200x200")
root.title(f + " - atripad")
t = Text(root, font="calibiri" + sizestr)
t.pack(side = BOTTOM,fill=BOTH)
m = Menu(root)
m2 = Menu(root)
fm = Menu(m, tearoff=0)
fm.add_command(label="New", command=new)
fm.add_command(label="Open", command=opennew)
fm.add_command(label="Save", command=save)
fm.add_command(label="Save As", command=saveas)
fm.add_separator()
fm.add_command(label="Quit", command=quitGUI)

em = Menu(m, tearoff=0)
em.add_command(label="Cut", command=cut)
em.add_command(label="Copy", command=copy)
em.add_command(label="Paste", command=paste)
# em.add_command(label="edit style", command=searchi)
am = Menu(m)
am.add_command(label="About Me", command=abm)

m.add_cascade(label="File", menu=fm)
m.add_cascade(label="Edit", menu=em)
m.add_cascade(label="Credits", menu=am)
root.config(menu=m)
# s = Scrollbar()# real signature unknown
# t.yview_scroll(s.get(),"units")
# s.set(t.yview(),t.yview())
# root.config(menu=m2)
root.mainloop()
