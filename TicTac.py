from tkinter import *
from tkinter import messagebox

class TicTac:
    def __init__(self,root):
        self.c=0
        self.f=Frame(root,width=500,height=500)
        self.f.propagate(0)
        self.f.pack()
        self.b1=Button(self.f,width=3,font=('Times -40 bold'),command=lambda : self.on_click(1))
        self.b2=Button(self.f,width=3,font=('Times -40 bold'),command=lambda : self.on_click(2))
        self.b3=Button(self.f,width=3,font=('Times -40 bold'),command=lambda : self.on_click(3))
        self.b4=Button(self.f,width=3,font=('Times -40 bold'),command=lambda : self.on_click(4))
        self.b5=Button(self.f,width=3,font=('Times -40 bold'),command=lambda : self.on_click(5))
        self.b6=Button(self.f,width=3,font=('Times -40 bold'),command=lambda : self.on_click(6))
        self.b7=Button(self.f,width=3,font=('Times -40 bold'),command=lambda : self.on_click(7))
        self.b8=Button(self.f,width=3,font=('Times -40 bold'),command=lambda : self.on_click(8))
        self.b9=Button(self.f,width=3,font=('Times -40 bold'),command=lambda : self.on_click(9))
        self.rs=Button(self.f,width=4,command=self.reset,text='Reset')
        self.b1.grid(row=0,column=0)
        self.b2.grid(row=0,column=1)
        self.b3.grid(row=0,column=2)
        self.b4.grid(row=1,column=0)
        self.b5.grid(row=1,column=1)
        self.b6.grid(row=1,column=2)
        self.b7.grid(row=2,column=0)
        self.b8.grid(row=2,column=1)
        self.b9.grid(row=2,column=2)
        self.rs.grid(row=3,column=2,pady=10)
    def on_click(self,i):
        if i==1 :
            if self.c%2==0 :
                self.b1['text']='O'
            else :
                self.b1['text']='X'
            self.b1.config(command=lambda:self.on_click(10))
        elif i==2 :
            if self.c%2==0 :
                self.b2['text']='O'
            else :
                self.b2['text']='X'
            self.b2.config(command=lambda:self.on_click(10))
        elif i==3 :
            if self.c%2==0 :
                self.b3['text']='O'
            else :
                self.b3['text']='X'
            self.b3.config(command=lambda:self.on_click(10))
        elif i==4 :
            if self.c%2==0 :
                self.b4['text']='O'
            else :
                self.b4['text']='X'
            self.b4.config(command=lambda:self.on_click(10))
        elif i==5 :
            if self.c%2==0 :
                self.b5['text']='O'
            else :
                self.b5['text']='X'
            self.b5.config(command=lambda:self.on_click(10))
        elif i==6 :
            if self.c%2==0 :
                self.b6['text']='O'
            else :
                self.b6['text']='X'
            self.b6.config(command=lambda:self.on_click(10))
        elif i==7 :
            if self.c%2==0 :
                self.b7['text']='O'
            else :
                self.b7['text']='X'
            self.b7.config(command=lambda:self.on_click(10))
        elif i==8 :
            if self.c%2==0 :
                self.b8['text']='O'
            else :
                self.b8['text']='X'
            self.b8.config(command=lambda:self.on_click(10))
        elif i==9 :
            if self.c%2==0:
                self.b9['text']='O'
            else :
                self.b9['text']='X'
            self.b9.config(command=lambda:self.on_click(10))
        self.c+=1
        self.win()
    def win(self):
        if self.b1['text']==self.b2['text']==self.b3['text']=='O' or self.b4['text']==self.b5['text']==self.b6['text']=='O' or self.b7['text']==self.b8['text']==self.b9['text']=='O' or self.b1['text']==self.b4['text']==self.b7['text']=='O' or self.b2['text']==self.b5['text']==self.b8['text']=='O'or self.b3['text']==self.b6['text']==self.b9['text']=='O' or self.b1['text']==self.b5['text']==self.b9['text']=='O' or self.b3['text']==self.b5['text']==self.b7['text']=='O':
            messagebox.showinfo('Win','O wins')
            self.reset()
        if self.b1['text']==self.b2['text']==self.b3['text']=='X' or self.b4['text']==self.b5['text']==self.b6['text']=='X' or self.b7['text']==self.b8['text']==self.b9['text']=='X' or self.b1['text']==self.b4['text']==self.b7['text']=='X' or self.b2['text']==self.b5['text']==self.b8['text']=='X'or self.b3['text']==self.b6['text']==self.b9['text']=='X' or self.b1['text']==self.b5['text']==self.b9['text']=='X' or self.b3['text']==self.b5['text']==self.b7['text']=='X':
            messagebox.showinfo('Win','X wins')
            self.reset()
    def reset(self):
        self.b1['text']=self.b2['text']=self.b3['text']=self.b4['text']=self.b5['text']=self.b6['text']=self.b7['text']=self.b8['text']=self.b9['text']=''
        self.b1.config(command=lambda:self.on_click(1))
        self.b2.config(command=lambda:self.on_click(2))
        self.b3.config(command=lambda:self.on_click(3))
        self.b4.config(command=lambda:self.on_click(4))
        self.b5.config(command=lambda:self.on_click(5))
        self.b6.config(command=lambda:self.on_click(6))
        self.b7.config(command=lambda:self.on_click(7))
        self.b8.config(command=lambda:self.on_click(8))
        self.b9.config(command=lambda:self.on_click(9))
        self.c=0

root=Tk()
obj=TicTac(root)
root.mainloop()
