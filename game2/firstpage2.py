from tkinter import *
import random
import time


#class ball is for the creation of the ball
#canvas  in class ball is used in drawing
class Ball:
    def __init__(self, canvas):
        self.canvas = canvas
        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width = self.canvas.winfo_width()
        canvas.bind_all('<KeyPress-Up>', self.up)
        canvas.bind_all('<KeyPress-Down>',self.down)
        canvas.bind_all('<KeyPress-Left>',self.left)
        canvas.bind_all('<KeyPress-Right>',self.right)

    def left(self, evt):
         exec(open('game.py').read())
         self.canvas.destroy()
    def right(self, evt):
        exec(open('game3.py').read())
    def down(self, evt):
         self.y = -2
    def up(self, evt):
        self.y = 2





        


    


tk = Tk()
#this creates a name for the window, it is called the title fuction
tk.title("welcome")
#we use resizable to make the window fixed(cannot be changed) horizantally and vertically
tk.resizable(0, 0)
#?
tk.wm_attributes("-topmost", 1)
canvas = Canvas(tk, width=500, height=400, bd=0, highlightthickness=0)
canvas.pack()
tk.update()


#the ball is created
ball = Ball(canvas)
