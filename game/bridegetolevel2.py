from tkinter import *
import time

time.sleep(3)
yourscore = Tk()
yourscore.title("Your score")
yourscore.wm_attributes("-topmost", 1)
thescore = Canvas(yourscore, width=500, height=400, bd=0, highlightthickness=0)
score_text = thescore.create_text(250, 200, text='CONGRATULATIONS! \n  YOU WIN \n  \n your score is :' +str(score.finalscore()), state='hidden')
thescore.itemconfig(score_text, state='normal')
thescore.pack()
