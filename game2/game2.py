
import time
import random

#tkinter is a module used to create apps with more animation and graphics
#tkinter is a module which helps in drawing on screens 
from tkinter import *




class Ball:
    #we used canvas as a parameter because we will use as object and draw on it
    #canvas is an object  of class Class canvas inside thinkter module
    #canvas is used in drawing things( e.g shapes)
    def __init__(self, canvas):
        self.canvas = canvas
        self.id=canvas.create_oval(10, 10, 25, 25,fill='red')


canvas = Canvas( width=500, height=400, bd=0, highlightthickness=0)
canvas.pack()


#the ball is created
ball = Ball(canvas)
