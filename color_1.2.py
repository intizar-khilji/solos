# Dependency -> Install pillow module
# pip install pillow

from tkinter import *
import random
import os
import urllib.request as req
try :
    from PIL import Image, ImageTk
except:
    os.system('pip3 install pillow')
    from PIL import Image, ImageTK

list = os.listdir()
if 'color.png' not in list:
    req.urlretrieve('https://i1.wp.com/www.ed2go.com/blog/wp-content/uploads/2015/01/Color-Logo-Design-Tips.png', 'color.png')
    print('Image Downloaded.')

class color:
    def __init__(self,root):
        # Declaring Variables
        self.TIME = 60
        self.SPEED = 1000
        self.SCORE = 0
        self.RANDOM1 = random.randint(0,8)
        self.RANDOM2 = random.randint(0,8)
        self.COLOR_LOGO_PATH = 'color.png'
        self.COLOR_TEXT_FONT = ('Monotype Corsiva', -55, 'bold')
        self.ID = None
        self.START_FLAG = True

        # Creating Image object for logo
        self.COLOR_LOGO_IMAGE = ImageTk.PhotoImage(Image.open(self.COLOR_LOGO_PATH).resize((150,70)), Image.ANTIALIAS)
        # Declaring Colors and Their Names
        self.COLORS_ON_TEXT = ('red','green','pink','white','black','blue','yellow','orange','purple','brown')
        self.COLORS_NAME = ('red','green','pink','white','black','blue','yellow','orange','purple','brown')


        # Declaring frames 
        self.frame = Frame(root, height=420, width=300)
        self.frame.propagate(0)
        self.frame.pack()
        
        # Declaring Widget
        self.logolabel = Label(self.frame, image = self.COLOR_LOGO_IMAGE)
        self.logolabel.pack(pady=10)
        self.gamelabel = Label(self.frame, text='GAME', font=('Bahnschrift Condensed', -40, 'bold'))
        self.gamelabel.pack()
        self.messagelabel = Label(self.frame, text='TYPE THE COLOR OF THE WORDS\nNOT THE WORD TEXT', font=('Times New Roman', -15, 'bold'), foreground='skyblue')
        self.messagelabel.pack()
        self.scorelabel = Label(self.frame, text='SCORE: 0', font=('Times New Roman', -20, 'bold'))
        self.scorelabel.pack()
        self.timeleftlabel = Label(self.frame, text='TIME LEFT: 0', font=('Times New Roman', -15))
        self.timeleftlabel.pack()
        self.colorlabel = Label(self.frame, text='-----------', font=self.COLOR_TEXT_FONT)
        self.colorlabel.pack()
        self.textlabel = Label(self.frame, text='ENTER COLOR BELOW :', font=('Times New Roman', -15))
        self.textlabel.pack()
        self.entry = Entry(self.frame)
        self.entry.pack()
        self.startbutton = Button(self.frame, text='Start', font=('Times New Roman', -20), width=10)
        self.startbutton.pack(pady=10)
        self.entry.bind('<Return>', self.check)

        self.startbutton.bind('<Button-1>', self.startx)

    def startx(self, event):
        if self.START_FLAG :
            self.entry.focus_set()
            self.colorlabel.config(text=self.COLORS_NAME[self.RANDOM1], foreground=self.COLORS_ON_TEXT[self.RANDOM2])
            self.START_FLAG = not self.START_FLAG
        self.timeleftlabel.config(text=f'TIME LEFT: {self.TIME}')
        if self.TIME == 0:
            messagebox.showinfo('Game Over',f'Your Score : {self.SCORE}')
            self.SCORE = 0
            self.TIME = 60
            self.timeleftlabel.after_cancel(self.ID)
            self.START_FLAG = True
        else:
            self.TIME=self.TIME-1
            self.ID = self.timeleftlabel.after(1000, lambda: self.startx(event))
    
    def check(self, event):
        COMPARE = self.COLORS_ON_TEXT[self.RANDOM2]
        self.RANDOM1 = random.randint(0,9)
        self.RANDOM2 = random.randint(0,9)
        if self.TIME > 0 and self.entry.get() != '':
            self.colorlabel.config(text=self.COLORS_NAME[self.RANDOM1], foreground=self.COLORS_ON_TEXT[self.RANDOM2])
            if COMPARE == self.entry.get():
                self.SCORE += 1
            else:
                self.SCORE -= 1
            self.entry.delete(0,END)
        self.scorelabel.config(text=f'SCORE: {self.SCORE}')
    

root = Tk()
root.title('CoLoR')
obj = color(root)
root.mainloop()