#refer to python for kids pg194

#tkinter is a module used for graphics
import time
import random
from tkinter import *

level=int(input("enter the level :"))
if level==1:
    
    #class ball is for the creation of the ball
#canvas  in class ball is used in drawing
    class Ball:
        def __init__(self, canvas, color):
            self.canvas = canvas
            #color and shape of the ball in wich 10 and 10 are x coordinates right and left and 25 and 25 are y coordinates up and down and color for the filling the color
            self.id = canvas.create_oval(10, 10, 25, 25, fill=color)
            #positions the ball
            self.canvas.move(self.id, 245, 100)
            '''#updated1
            self.x = 0
            self.y = -1'''
            #makes the ball start anywhere randomly
            starts = [-3, -2, -1, 1, 2, 3]
            random.shuffle(starts)
            self.x = starts[0]
            self.y = -3
            self.canvas_height = self.canvas.winfo_height()
            self.canvas_width = self.canvas.winfo_width()
            canvas.bind_all('<KeyPress-Up>', self.up)
            canvas.bind_all('<KeyPress-Down>',self.down)
            canvas.bind_all('<KeyPress-Left>',self.left)
            canvas.bind_all('<KeyPress-Right>',self.right)
        

        def draw(self):
            #calls the move functiona and 0 will stop the ball from moving horizantally and  -1 will make the ball to move 1px up the screen
            '''self.canvas.move(self.id, 0, -1)'''
            #updated1
            self.canvas.move(self.id, self.x, self.y)
            #This function (canvas.coords)returns the current x and y coordinates of anything drawn on the canvas
            pos = self.canvas.coords(self.id)

        #after the canvas.coords function have done the job of giving the coordinates then...
            '''#from the coordinates,if the ball hits the top of the screen  then stop moving up
            if pos[1] <= 0:
                self.y = 1
            #from the coordinates,if the ball hits the bottom of the screen  then stop moving down
            if pos[3] >= self.canvas_height:
                self.y = -1'''

            if pos[1] <= 0:
                self.y = 3
            if pos[3] >= self.canvas_height:
                self.y = -3
            if pos[0] <= 0:
                self.x = 3
            if pos[2] >= self.canvas_width:
                self.x = -3

    #below are functions for controlling the ball
        def left(self, evt):
            self.x = -2
        def right(self, evt):
            self.x = 2
        def down(self, evt):
            self.y = -2
        def up(self, evt):
            self.y = 2
    
    tk = Tk()
    #this creates a name for the window, it is called the title fuction
    tk.title("Game level 1")
    #we use resizable to make the window fixed(cannot be changed) horizantally and vertically
    tk.resizable(0, 0)
    #?
    tk.wm_attributes("-topmost", 1)
    canvas = Canvas(tk, width=500, height=400, bd=0, highlightthickness=0)
    canvas.pack()
    tk.update()


    #the ball is created
    ball = Ball(canvas, 'red')





    #the below bunch of codes is responsible for redrawing the ball(using loop) 
    while 1:
        ball.draw()
        tk.update_idletasks()
        tk.update()
        #time.sleep is a call to sleep function which which tells python to sleep in the 0.01 second
        #time taken for the ball to vanish 
        time.sleep(0.01)

    
elif level==2:
   



#class ball is for the creation of the ball
#canvas  in class ball is used in drawing
    class Ball:
        def __init__(self, canvas, color):
            self.canvas = canvas
            #color and shape of the ball in wich 10 and 10 are x coordinates right and left and 25 and 25 are y coordinates up and down and color for the filling the color
            self.id = canvas.create_oval(10, 10, 25, 25, fill=color)
            #positions the ball
            self.canvas.move(self.id, 245, 100)
            '''#updated1
            self.x = 0
            self.y = -1'''
            #makes the ball start anywhere randomly
            starts = [-3, -2, -1, 1, 2, 3]
            random.shuffle(starts)
            self.x = starts[0]
            self.y = -3
            self.canvas_height = self.canvas.winfo_height()
            self.canvas_width = self.canvas.winfo_width()
            canvas.bind_all('<KeyPress-Up>', self.up)
            canvas.bind_all('<KeyPress-Down>',self.down)
            canvas.bind_all('<KeyPress-Left>',self.left)
            canvas.bind_all('<KeyPress-Right>',self.right)
        

        def draw(self):
            #calls the move functiona and 0 will stop the ball from moving horizantally and  -1 will make the ball to move 1px up the screen
            '''self.canvas.move(self.id, 0, -1)'''
            #updated1
            self.canvas.move(self.id, self.x, self.y)
            #This function (canvas.coords)returns the current x and y coordinates of anything drawn on the canvas
            pos = self.canvas.coords(self.id)

        #after the canvas.coords function have done the job of giving the coordinates then...
            '''#from the coordinates,if the ball hits the top of the screen  then stop moving up
            if pos[1] <= 0:
                self.y = 1
            #from the coordinates,if the ball hits the bottom of the screen  then stop moving down
            if pos[3] >= self.canvas_height:
                self.y = -1'''

            if pos[1] <= 0:
                self.y = 3
            if pos[3] >= self.canvas_height:
                self.y = -3
            if pos[0] <= 0:
                self.x = 3
            if pos[2] >= self.canvas_width:
                self.x = -3

    #below are functions for controlling the ball
        def left(self, evt):
            self.x = -2
        def right(self, evt):
            self.x = 2
        def down(self, evt):
            self.y = -2
        def up(self, evt):
            self.y = 2
    
    tk = Tk()
    #this creates a name for the window, it is called the title fuction
    tk.title("Game level 2")
    #we use resizable to make the window fixed(cannot be changed) horizantally and vertically
    tk.resizable(0, 0)
    #?
    tk.wm_attributes("-topmost", 1)
    canvas = Canvas(tk, width=500, height=400, bd=0, highlightthickness=0)
    canvas.pack()
    tk.update()


    #the ball is created
    ball = Ball(canvas, 'red')





    #the below bunch of codes is responsible for redrawing the ball(using loop) 
    while 1:
        ball.draw()
        tk.update_idletasks()
        tk.update()
        #time.sleep is a call to sleep function which which tells python to sleep in the 0.01 second
        #time taken for the ball to vanish 
        time.sleep(0.01)




