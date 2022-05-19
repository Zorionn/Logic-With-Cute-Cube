
#------Import-------------------
from tkinter import *
from tkinter.font import Font
from tkinter import ttk
import tkinter.messagebox as mbox
from tkinter import simpledialog
import datetime
import tkcalendar
import sys

#------Main Directory---------------------------
class app:
    def __init__(self,window):
        self.window = window
        window.title("Income and Expense")
        window.geometry("800x600")
        self.your_name = "Your name"
        self.name_in = StringVar()
        self.last_name = StringVar()
        header_size = Font(size=17,weight="bold")
        size = Font(size=14,weight="bold")
        act_list = ['Date','Category','Amount']
        rec_list = ['Date','Amount']
        self.money = 0
        self.nemoney = 0
        

        #----------frame-------------------------------------------------
        self.frame_bg = Frame(window, width = 800, height = 600, bg = "#FAFCFA")
        self.frame_bg2 = Frame(window, width = 800, height = 600, bg = "#FAFCFA")
        self.frame_bg3 = Frame(window, width = 800, height = 600, bg = "#FAFCFA")
        self.frame_left = Frame(window, width = 240, height =590, bg = "#CCFFB8")
        self.frame_gnd = Frame(window, width = 545,height = 150, bg = "#CCFFB8")
        self.frame_in = Frame(self.frame_bg, width = 100,height = 40, bg = "#CCFFB8")
        self.frame_out = Frame(self.frame_bg, width = 100,height = 40, bg = "#F08383")
        self.frame_bal = Frame(self.frame_bg, width = 100,height = 40, bg = "#9AEDFC")
        
    

        self.frame_bg.place(x=0,y=0)
        self.frame_left.place(x=5,y=5)
        self.frame_gnd.place(x=250,y=445)
        self.frame_in.place( x = 250,y=50)
        self.frame_out.place( x = 250,y=145)
        self.frame_bal.place( x = 250,y=245)
    
        #--------Main Menu--------------------------------------------------
        self.welcome = Label(self.frame_bg,text= ("Welcome"+" "+self.your_name),font = header_size,bg = "#FAFCFA",fg = "black")
        self.income = Label(self.frame_in,text="Income",font = size,bg = "#CCFFB8",fg = "black")
        self.outcome = Label(self.frame_bg,text="Expense",font = size,bg = "#F08383",fg = "black")
        self.balance = Label(self.frame_bg,text="Balance",font = size,bg = "#9AEDFC",fg = "black")
        self.report = Label(self.frame_bg,text="Recent activity",font = header_size,bg = "#FAFCFA",fg = "black")
        self.incomebut = Button(self.frame_gnd,width =20, height =2,bg = "#28FF00",text="Add Income",command = self.input)
        self.outcomebut = Button(self.frame_gnd,width =20, height =2,bg = "#FF0000",text="Add Expense",command = self.expense)
        self.current = Label(self.frame_bg,text = self.money,font = header_size,bg = "#FAFCFA",fg = "black")
        self.necurrent = Label(self.frame_bg,text = self.nemoney,font = header_size,bg = "#FAFCFA",fg = "black")
        self.dif = Label(self.frame_bg,text = self.money - self.nemoney,font = header_size,bg = "#FAFCFA",fg = "black")
        self.rec = ttk.Treeview(self.frame_bg,column = rec_list,show ='headings', height=5)
        for i in rec_list:
            self.rec.heading(i, text = i.title())

        self.welcome.place(x = 250, y=10)
        self.income.place(x = 5, y =5)
        self.outcome.place(x = 250, y = 150)
        self.balance.place(x = 250, y = 250)
        self.report.place(x= 500, y = 50)
        self.incomebut.place(x = 200, y= 20)
        self.outcomebut.place(x=200,y=70)
        self.current.place(x = 250, y = 100)
        self.necurrent.place(x = 250, y = 200)
        self.dif.place(x = 250, y =300)
        self.rec.place(x = 400,y =100)

        #--------History------------------------------------------------
        self.header = Label(self.frame_bg2,text= "History",font = header_size,bg = "#FAFCFA",fg = "black")
        self.act = ttk.Treeview(self.frame_bg2,column = act_list,show ='headings', height=20)
        for i in act_list:
            self.act.heading(i, text = i.title())
        self.remove_one = Button(self.frame_bg2,width = 20, height = 2,bg = "#CCFFB8",text="Remove",command = self.remove_one)
        self.remove_many = Button(self.frame_bg2,width = 20, height = 2,bg = "#CCFFB8",text="Remove many",command = self.remove_many)
        self.remove_all = Button(self.frame_bg2,width = 20, height = 2,bg = "#CCFFB8",text="Remove all",command = self.remove_all)

        self.header.place(x = 250, y = 10)
        self.act.place(x = 250, y = 50)
        self.remove_one.place(x = 250, y =500)
        self.remove_all.place(x = 400, y= 500)
        self.remove_many.place(x = 550, y= 500)

        #--------Setting-------------------------------------------------
        self.header_setting = Label(self.frame_bg3,text= "Setting",font = header_size,bg = "#FAFCFA",fg = "black")
        self.name = Label(self.frame_bg3,text = "Enter your first name",font = header_size,bg = "#FAFCFA",fg = "black")
        self.last_name1 = Label(self.frame_bg3,text = "Enter your last name",font = header_size,bg = "#FAFCFA",fg = "black")
        self.entry = Entry(self.frame_bg3,width = 20,font=(None,18),textvariable = self.name_in)
        self.entry1 = Entry(self.frame_bg3,width = 20,font=(None,18),textvariable = self.last_name)
        self.save = Button(self.frame_bg3,width =20, height =2,bg = "#CCFFB8",text="Save",command = self.chage)
        self.quit = Button(self.frame_bg3,width =20, height =2,bg = "#CCFFB8",text="Quit",command = self.exit_o)
        self.date = tkcalendar.DateEntry(self.frame_bg3,width =18,backgroud ='blue',foreground='white')
        


        self.header_setting.place(x = 500, y =10)
        self.name.place(x=250, y= 50)
        self.last_name1.place(x=250,y=90)
        self.entry.place(x = 550, y = 50)
        self.entry1.place(x = 550, y = 90)
        self.save.place(x = 500, y =500)
        self.quit.place(x = 250, y =500)
        self.date.place(x = 250,y = 200)

        #---------Taskbar-----------------------------------------------------
        self.Menu = Button(self.frame_left,width =20, height =2,bg = "#CCFFB8",text="Main Menu",command = self.main_menu)
        self.history = Button(self.frame_left,width =20, height =2,bg = "#CCFFB8",text="History",command = self.history)
        self.setting = Button(self.frame_left,width =20, height =2,bg = "#CCFFB8",text="Setting",command = self.setting)

        self.Menu.place(x=10,y=10)
        self.history.place(x=10,y=110)
        self.setting.place(x=10,y=210)

    def input(self):
        inputa = simpledialog.askinteger("Enter income","please enter your income")
        inputc = simpledialog.askstring("Enter Category","please enter category")
        now = self.date.get()
        a = inputa
        income = [now,inputc,+a]
        rec_i = [now,+a]
        self.money += a
        self.current.config(text = self.money)
        self.dif.config(text = self.money - self.nemoney)
        self.act.insert('','end',values=income)
        self.rec.insert('','end',value=rec_i)

    def expense(self):
        inputa = simpledialog.askinteger("Enter Expense","please enter your Expense")
        inputc = simpledialog.askstring("Enter Category","please enter category")
        now = self.date.get()
        a = inputa
        expense = [now,inputc,-a]
        rec_e = [now,-a]
        self.nemoney += a
        self.necurrent.config(text = self.nemoney)
        dif = self.money - self.nemoney
        self.dif.config(text = dif)
        self.act.insert('','end',values=expense)
        self.rec.insert('','end',value=rec_e)

    def history(self):
        self.frame_bg.pack_forget()
        self.frame_bg.place(x=800,y= 0)
        self.frame_bg3.place(x=800,y= 0)
        self.frame_bg2.place(x=0,y= 0)
        self.frame_gnd.place(x=800,y=0)

    def main_menu(self):
        self.frame_bg2.place(x=800,y= 0)
        self.frame_bg3.place(x=800,y=0)
        self.frame_bg.place(x=0,y= 0)
        self.frame_gnd.place(x=250,y=445)

    def setting(self):
        self.frame_bg.place(x=800,y= 0)
        self.frame_bg2.place(x=800,y= 0)
        self.frame_bg3.place(x=0,y= 0)
        self.frame_gnd.place(x=800,y=0)

    def chage(self):
        self.your_name = self.name_in.get()
        last_name = self.last_name.get()
        self.welcome.config(text = ("Welcome"+ " " +self.your_name+" "+last_name))
        self.entry.delete(0, END)
        self.entry1.delete(0, END)

    def remove_one(self):
        x = self.act.selection()[0]
        val = self.rec.item(x)['values'][1]
        self.act.delete(x)
        self.rec.delete(x)
        if val < 0:
            necur = self.nemoney + val
            self.nemoney = necur
            self.dif.config(text = self.money + self.nemoney)
            self.necurrent.config(text = necur)
            
        else :
            cur = self.money - val
            self.money = cur
            self.dif.config(text = self.money - self.nemoney)
            self.current.config(text = cur)
        

    def remove_all(self):
        for i in self.act.get_children():
            self.act.delete(i)
        for j in self.rec.get_children():
            self.rec.delete(j)
        self.current.config(text = 0)
        self.money = 0
        self.nemoney = 0
        self.dif.config(text = 0)
        self.necurrent.config(text = 0)

    def exit_o(self):
        ans = mbox.askyesno('Exit','Are you sure?')
        if ans:
            self.window.destroy()

    def remove_many(self):
        x = self.act.selection()
        for i in x:
            self.act.delete(i)
            self.rec.delete(i)

        
        
        


root = Tk()
m = app(root)

root.mainloop()