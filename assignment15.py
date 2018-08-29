question no.1


"
from tkinter import *
root=Tk()
root.geometry("800x800")
root.title("My first application")


f1=Frame(root,height=400,width=500,bg="red")
f1.pack(side=TOP)

lbl=Label(f1, text="HELLO WORLD",font=('ALGERIAN',40,'bold'),bd=20,bg="Green",fg="yellow")
lbl.pack()

f2=Frame(root,height=80,width=400,bg="red")
f2.pack(side=LEFT)

button=Button(f2, text='stop',width=25,command=quit)
button.pack()


"

question no.2

"
from tkinter import *


root=Tk()


root.geometry("800x800")
root.title("My first application")


def text():
    label.config(text="hello iam here")


f1=Frame(root,height=400,width=500,bg="red")
f1.pack(side=TOP)

label=Label(f1,font=("ALGERIAN",50))
label.pack()


button=Button(f1, text='stop',width=25,command=text)
button.pack()

"

question no.3

"
from tkinter import *


root=Tk()


root.geometry("800x800")
root.title("My first application")


def text():
    label.config(text="hello iam here")


f1=Frame(root,height=400,width=500,bg="red")
f1.pack(side=TOP)

label=Label(f1,font=("ALGERIAN",50),text="Click ME")
label.pack()


button=Button(f1, text='Magic show',width=25,command=text)
button.pack()
button1=Button(f1, text='Exit',width=25,command=quit)
button1.pack()

root.mainloop()

"


question no.4

"
from tkinter import *


root=Tk()



root.title("My first application")


def show():
    print('your status is %s'%(e.get()))
l1=Label(root,text="enter something").grid(row=0)

e=Entry(root,font=("arial",20),bd=20,bg='Grey',justify="right",text=l1)
e.grid(row=0,column=0)


button=Button(root, text='Magic show',width=25,command=show)
button.grid()


root.mainloop()


"