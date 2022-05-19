from tkinter import *
from tkinter import messagebox
import random

class typing:
    def __init__(self,window):
        self.window=window
        self.window.title("Typing game")
        self.window.geometry("250x200")
        
        labelling=Label(self.window,text="Typing game")
        labelling.place(x=75,y=0)
        self.easy_mode=Button(self.window,text="EASY",command=lambda : self.start(1))
        self.easy_mode.place(x=80,y=30)
        self.norm_mode=Button(self.window,text="NORMAL",command=lambda : self.start(2))
        self.norm_mode.place(x=80,y=60)
        self.hard_mode=Button(self.window,text="HARD",command=lambda : self.start(3))
        self.hard_mode.place(x=80,y=90)
        rule=Button(self.window,text="RULES",command=self.rules)
        rule.place(x=80,y=120)
        exit=Button(self.window,text="EXIT",command=self.exit_pro)
        exit.place(x=80,y=150)

    def start(self,number):
        self.easy_mode.destroy()
        self.norm_mode.destroy()
        self.hard_mode.destroy()
        lives=3
        score=0
        highscore=0
        seconds=60
        
        self.play=Toplevel()
        self.play.geometry("300x200")

        if number==1:
            self.play.title("EASY")
            file=open("EasyWord.txt","r")
        if number==2:
            self.play.title("NORMAL")
            file=open("NormWord.txt","r")
        if number==3:
            self.play.title("HARD")
            file=open("HardWord.txt","r")
            
        line=file.readline()
        self.list_word=line.split()
        self.tempword=random.choice(self.list_word)
        self.pre=Label(self.play,text="Word:")
        self.pre.place(x=0,y=0)
        self.word_rand=Label(self.play,text=self.tempword)
        self.word_rand.place(x=40,y=0)

        self.lab_hi=Label(self.play,text="High score:")
        self.lab_hi.place(x=120,y=0)
        self.high_score=Label(self.play,text=highscore)
        self.high_score.place(x=185,y=0)

        self.time_lab=Label(self.play,text="Time:")
        self.time_lab.place(x=220,y=0)
        self.second=Label(self.play,text=seconds)
        self.second.place(x=260,y=0)

        self.lab_live=Label(self.play,text="Live:")
        self.lab_live.place(x=0,y=25)
        self.lives_count=Label(self.play,text=lives)
        self.lives_count.place(x=30,y=25)

        self.lab_score=Label(self.play,text="Score:")
        self.lab_score.place(x=120,y=25)
        self.score_number=Label(self.play,text=score)
        self.score_number.place(x=160,y=25)
        
        self.lab_word=Label(self.play,text="Type:")
        self.lab_word.place(x=0,y=50)

        self.enter1=StringVar()
        self.entered_word=Entry(self.play,textvariable=self.enter1)
        self.entered_word.place(x=50,y=50)
        
        self.reset=Button(self.play,text="reset",command=self.reset)
        self.reset.place(x=0,y=100)
        
        self.delete=Button(self.play,text="close all",command=self.window.destroy)
        self.delete.place(x=0,y=150)

        self.play.after(1000,self.timeminus)
        self.play.bind('<Return>',self.checking_ans)
        self.play.mainloop()

    def checking_ans(self,event):
        list=self.list_word
        ans=self.enter1.get()
        word=self.word_rand.cget("text")
        sc=self.score_number.cget("text")
        li=self.lives_count.cget("text")
        ti=self.second.cget("text")
        hi=self.high_score.cget("text")
        live_type=isinstance(li,int)
        if live_type==True or ti==0:
            if li > 0:
                if word==ans:
                    sc=sc+1
                    self.score_number.config(text=sc)
                    if sc>=hi:
                        self.high_score.config(text=sc)
                if word!=ans:
                    li=li-1
                    self.lives_count.config(text=li)
                self.entered_word.delete(0,'end')
                self.word_rand.config(text=random.choice(list))
            if li==0:
                messagebox.showinfo("0","Out of lives,reset or exit to play")
                self.lives_count.config(text="Out of live")
                self.second.config(text=0)
        else:
            messagebox.showinfo("0","Out of lives,reset or exit game")
        
    def timeminus(self):
        sec=self.second.cget("text")
        sec=sec-1
        self.second.config(text=sec)
        if sec > 0:
            self.play.after(1000,self.timeminus)
        if sec == 0:
            lives=0
            self.lives_count.config(text=lives)
            messagebox.showinfo("Timeout","Out of time")

    def reset(self):
        temp=self.second.cget("text")
        liv=self.lives_count.cget("text")
        if temp!=0 and liv!="Out of live":
            messagebox.showinfo("Time","time does not ran out")
        if temp==0 or liv=="Out of live":           
            lives=3
            score=0
            seconds=60
            self.score_number.config(text=score)
            self.lives_count.config(text=lives)
            self.entered_word.delete(0,'end')
            self.second.config(text=seconds)
            self.play.after(1000,self.timeminus)

    def rules(self):
        messagebox.showinfo('RULE',
                            '1.You have 3 live.When enter wrong answer -1 live\n'
                            '2.For each correct you get +1 score\n'
                            '3.If live=0 game is over you need to reset or exit the program\n'
                            '4.easy=3 letters,normal=4-5 letters,hard=6-7 letters\n'
                            '5.This program answer checking is case sensitive')
        
    def exit_pro(self):
        self.window.destroy()        
        
root=Tk()
start=typing(root)
root.mainloop()
