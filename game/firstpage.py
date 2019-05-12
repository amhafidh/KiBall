from tkinter import *

def level(x):
    file1=open(x)
    first=file1.read()
    exec (first)


welcome = Tk()
welcome.title("welcome")
thepage = Canvas(welcome, width=500, height=400, bd=0, highlightthickness=0)
'''level1=open('game.py')
level1=level1.read()
level1=exec(level1)'''
btn1 = Button(welcome, width=10, height=5, text="level 1", command=level('game.py'))
btn1.pack()
btn1 = Button(welcome,width=10, height=5,  text="level 2", command=level('game1.py'))
btn1.pack()
thepage.pack()
