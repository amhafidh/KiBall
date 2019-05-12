try:
    #give 5 have demo for controlloing horizonatally and vertically. look at line 42

#refer to python for kids pg194


#tkinter is a module used for graphics

    from tkinter import *
    import random
    import time



    #class ball is for the creation of the ball
    #canvas  in class ball is used in drawing
    class Ball:
        def __init__(self, canvas,score, color):
            self.canvas = canvas
            self.score = score
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
            self.hit_bottom = False
            self.hit_up = False
            self.hit_right = False
            self.hit_left = False
            canvas.bind_all('<KeyPress-Up>', self.up)
            canvas.bind_all('<KeyPress-Down>',self.down)
            canvas.bind_all('<KeyPress-Left>',self.left)
            canvas.bind_all('<KeyPress-Right>',self.right)
            canvas.bind_all('<KeyPress-Return>', quit)

        def draw(self):
            #calls the move functiona and 0 will stop the ball from moving horizantally and  -1 will make the ball to move 1px up the screen
            '''self.canvas.move(self.id, 0, -1)'''
            #updated1
            #self.canvas.move(self.id, self.x, 0)
            self.canvas.move(self.id, 0, self.y)
            
            #This function (canvas.coords)returns the current x and y coordinates of anything drawn on the canvas
            pos = self.canvas.coords(self.id)
            #if self.y==-2 or self.y==2:
                #self.canvas.move(self.id,self.y, self.y)'''

            #after the canvas.coords function have done the job of giving the coordinates then...
            '''#from the coordinates,if the ball hits the top of the screen  then stop moving up
            if pos[1] <= 0:
                self.y = 1
            #from the coordinates,if the ball hits the bottom of the screen  then stop moving down
            if pos[3] >= self.canvas_height:
                self.y = -1'''

            if pos[1] <= 0:
                #self.y = 3
                self.hit_up = True
            if pos[3] >= self.canvas_height:
                self.hit_bottom = True
                #self.y = -3
            if pos[0] <= 0:
                self.hit_left = True
                #self.x = 3
            if pos[2] >= self.canvas_width :
                self.hit_right = True
                #self.x = -3


        #below are functions for controlling the ball
        def left(self, evt):
            self.x = -2
        def right(self, evt):
            self.x = 2
        def down(self, evt):
            self.y = -2
        def up(self, evt):
            self.y = 2
        
    class Score:
        def __init__(self, canvas, color):
            self.score = 0
            self.start=0
            self.start=time.time()
            self.canvas = canvas
            
            self.id = canvas.create_text(450, 10, text=self.score,fill=color)

        def scoreboard(self):            
            self.score +=1
            self.canvas.itemconfig(self.id, text=self.score)

        def finalscore(self):            
            return self.score

        def quit(event):
            print("Double Click, so let's stop") 
            import sys; sys.exit() 

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
    score = Score(canvas, 'blue')
    ball = Ball(canvas,score, 'red')
    game_over_text = canvas.create_text(250, 200, text='GAME OVER', state='hidden')
    firstime=time.time()
    #the below bunch of codes is responsible for redrawing the ball(using loop) 
    while 1:
        
        
        if ball.hit_bottom == False or ball.hit_up == False or ball.hit_right ==False or ball.hit_left ==False:
            ball.draw()
            if ball.hit_bottom != True or  ball.hit_up != True or ball.hit_right != True or ball.hit_left !=True :
                score.scoreboard()
        if time.time()- firstime>10.0:
            
            time.sleep(1)
            canvas.itemconfig(game_over_text, state='normal')
            canvas.destroy()
            yourscore = Tk()
            yourscore.title("Your score")
            yourscore.wm_attributes("-topmost", 1)
            thescore = Canvas(yourscore, width=500, height=400, bd=0, highlightthickness=0)
            #thescore.bind_all('<KeyPress-Return>', exec (nex()))
            #btn1 = Button(yourscore, width=10, height=5, text="level 1", command=exec(open('game.py').read()))
            #btn1.pack()
            score_text = thescore.create_text(250, 200, text='CONGRATULATIONS! \n  YOU WIN \n  \n your score is :' +str(score.finalscore()), state='hidden')
            thescore.itemconfig(score_text, state='normal')
            thescore.pack()

          
                
            
        '''thescore.itemconfig(score_text, state='normal')
            btn1 = Button(welcome, width=10, height=5, text="level 1", command=exec(open('game.py').read()))
            btn1.pack()'''
        if ball.hit_bottom == True or  ball.hit_up == True or ball.hit_right == True or ball.hit_left ==True :
            time.sleep(1)
            canvas.itemconfig(game_over_text, state='normal')
            canvas.destroy()
            yourscore = Tk()
            yourscore.title("Game Over")
            yourscore.wm_attributes("-topmost", 1)
            thescore = Canvas(yourscore, width=500, height=400, bd=0, highlightthickness=0)
            score_text = thescore.create_text(250, 200, text='GAME OVER ! \n  \n your score is :' +str(score.finalscore()), state='hidden')
            thescore.itemconfig(score_text, state='normal')
            thescore.pack()
            
            

        ball.draw()
        tk.update_idletasks()
        tk.update()
        
        #time.sleep is a call to sleep function which which tells python to sleep in the 0.01 second
        #time taken for the ball to vanish 
        time.sleep(0.05)
except:
    print("kipira game loading")
