from tkinter import *              
from tkinter import font  as tkFont 
import passman
from tkinter.ttk import Combobox
import tkinter.ttk as ttk
import random

class SampleApp(Tk):

    def __init__(self, *args, **kwargs):
        Tk.__init__(self, *args, **kwargs)
        
        self.geometry('800x450')
        self.minsize(800, 450)
        self.maxsize(800, 450)
        container = Frame(self)
        container.place(relx=0.5, rely=0.5, anchor=CENTER)

        self.frames = {}
        for F in (StartPage, LoginPage, RegisterPage, MainPage, Choice, GenPass):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="")
        

        self.show_frame("StartPage")

    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()
        frame.grid()
        for name,frameToDisable in self.frames.items():
            if name!=page_name:
                frameToDisable.grid_remove()



class StartPage(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.configure(bg='gray12')
        self.controller = controller
        registerbtn=Button(self, text='Register',width=20,height=3,
                bg='gray36',fg='lemon chiffon',
                 command=lambda: controller.show_frame("RegisterPage"))
        registerbtn.configure(font=('Calibri Light', 10))
        registerbtn.grid(row=0,column=0, padx=10)
        orlbl=Label(self,text="OR",bg='gray12', fg='lemon chiffon').grid(row=0,column=1)

        signinbtn=Button(self, text='Login', bg='gray36',fg='lemon chiffon' 
        ,width=20,height=3, command=lambda: controller.show_frame("LoginPage"))
        signinbtn.configure(font=('Calibri Light', 10))
        signinbtn.grid(row=0,column=2, padx=10)


class LoginPage(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller
        self.configure(bg='gray12')
        passman.initialize()
        loginTitle=Label(self, text="Login",bg='gray12', fg='lemon chiffon')
        loginTitle.configure(font=('Calibri Light', 20))
        loginTitle.grid(row=0, column=0, pady=20, columnspan=2)
        
        userlbl=Label(self,text='Username',bg='gray12', fg='lemon chiffon')
        userlbl.configure(font=('Calibri Light', 12))
        userlbl.grid(row=1, column=0, pady=5, padx=20)
        userfield=Entry(self, width=40)
        userfield.config({'background': 'gray80'})
        userfield.grid(row=1, column=1, pady=20)
        
        passlbl=Label(self,text='Password',bg='gray12', fg='lemon chiffon')
        passlbl.configure(font=('Calibri Light', 12))
        passlbl.grid(row=2, column=0, pady=5, padx=20)
        passfield=Entry(self,width=40)
        passfield.config({'background': 'gray80'})
        passfield.grid(row=2, column=1, pady=10)
        
        loginbtn=Button(self,width=20,text='Login',bg='gray36',fg='lemon chiffon',command=lambda: passman.login(userfield, passfield, controller))
        loginbtn.configure(font=('Calibri Light', 10))
        loginbtn.grid(row=3, columnspan=2, pady=20)
        backbtn=Button(self,width=10,text='Back',bg='gray36',fg='lemon chiffon',command=lambda: passman.backToStart(controller))
        backbtn.grid(row=4, columnspan=2, pady=10)


class Choice(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller
        self.configure(bg='gray12')
        credbtn=Button(self, text='Credentials',width=20,height=3,
                bg='gray36',fg='lemon chiffon',
                 command=lambda: controller.show_frame("MainPage"))
        credbtn.configure(font=('Calibri Light', 10))
        credbtn.grid(row=0,column=0, padx=10)
        orlbl=Label(self,text="OR",bg='gray12', fg='lemon chiffon').grid(row=0,column=1)

        genbtn=Button(self, text='Generate Password', bg='gray36',fg='lemon chiffon' 
        ,width=20,height=3, command=lambda: controller.show_frame("GenPass"))
        genbtn.configure(font=('Calibri Light', 10))
        genbtn.grid(row=0,column=2, padx=10)


class GenPass(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller=controller
        self.configure(bg='gray12')
        def low(): 
            entry.delete(0, END) 
        
            length = var1.get() 
        
            lower = "abcdefghijklmnopqrstuvwxyz"
            upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
            digits = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789 !@#$%^&*()"
            password = "" 
        
            if var.get() == 1: 
                for i in range(0, length): 
                    password = password + random.choice(lower) 
                return password 
        
            elif var.get() == 0: 
                for i in range(0, length): 
                    password = password + random.choice(upper) 
                return password 
        
            elif var.get() == 3: 
                for i in range(0, length): 
                    password = password + random.choice(digits) 
                return password 
            else: 
                print("Please choose an option") 
        
        
        def generate(): 
            password1 = low() 
            entry.insert(10, password1)  

        var = IntVar() 
        var1 = IntVar() 
        
        title=Label(self, text="Generate Password",bg='gray12', fg='lemon chiffon', pady=10)
        title.configure(font=('Calibri Light', 20))
        title.grid(row=0,column=0,padx=10,pady=5, columnspan=5)
        Random_password = Label(self, text="Password",bg='gray12', fg='lemon chiffon') 
        Random_password.grid(row=1,column=0,padx=10,pady=5) 
        entry = Entry(self)

        entry.grid(row=1, column=1,padx=10,pady=5) 
        
        c_label = Label(self, text="Length",bg='gray12',fg='lemon chiffon') 
        c_label.grid(row=2,column=0,padx=10,pady=5) 
        
        
        generate_button = Button(self, text="Generate", command=generate,bg='gray36',fg='lemon chiffon') 
        generate_button.configure(font=('Calibri Light', 10))
        generate_button.grid(row=2, column=2,columnspan=2,padx=10,pady=5)
        backbtn=Button(self,text='Back', width=5, bg='gray36',fg='lemon chiffon',command=lambda: passman.takeMeTo(controller, "Choice"))
        backbtn.configure(font=('Calibri Light', 10))
        backbtn.grid(row=2, column=3, padx=10, pady=5, columnspan=2) 
        
        myColor = 'gray12'                 
                

        s = ttk.Style()                     
        s.configure('Wild.TRadiobutton',background=myColor,foreground='lemon chiffon')   
        radio_low = ttk.Radiobutton(self, text="Low", variable=var, value=1,style = 'Wild.TRadiobutton')
        radio_low.grid(row=1, column=2, sticky='E',padx=10,pady=5) 
        radio_middle = ttk.Radiobutton(self, text="Medium", variable=var, value=0,style = 'Wild.TRadiobutton') 
        radio_middle.grid(row=1, column=3, sticky='E',padx=10,pady=5) 
        radio_strong = ttk.Radiobutton(self, text="Strong", variable=var, value=3,style = 'Wild.TRadiobutton') 
        radio_strong.grid(row=1, column=4, sticky='E',padx=10,pady=5) 
        combo = Combobox(self, textvariable=var1,width=17) 

        # Combo Box for length of your password 
        combo['values'] = (8, 9, 10, 11, 12, 13, 14, 15, 16, 
                        17, 18, 19, 20, 21, 22, 23, 24, 25, 
                        26, 27, 28, 29, 30, 31, 32, "Length") 

        combo.bind('<<ComboboxSelected>>') 
        combo.grid(column=1, row=2,padx=10,pady=5)

class RegisterPage(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller=controller
        self.configure(bg='gray12')
        registerTitle=Label(self, text="Register",bg='gray12', fg='lemon chiffon')
        registerTitle.configure(font=('Calibri Light', 20))
        registerTitle.grid(row=0, column=0, pady=20, columnspan=2)

        userlbl=Label(self,text='Username',bg='gray12', fg='lemon chiffon')
        userlbl.configure(font=('Calibri Light', 12))
        userlbl.grid(row=1, column=0, pady=5, padx=20)
        userfield=Entry(self, width=40)
        userfield.config({'background': 'gray80'})
        userfield.grid(row=1, column=1, pady=20)

        passlbl=Label(self,text='Password',bg='gray12', fg='lemon chiffon')
        passlbl.configure(font=('Calibri Light', 12))
        passlbl.grid(row=2, column=0, pady=5, padx=20)
        passfield=Entry(self,width=40)
        passfield.config({'background': 'gray80'})
        passfield.grid(row=2, column=1, pady=10)
        


        registerbtn=Button(self,width=20,text='Register',bg='gray36',fg='lemon chiffon', command=lambda: passman.createUser(userfield, passfield, controller))
        registerbtn.configure(font=('Calibri Light', 10))
        registerbtn.grid(row=3, columnspan=2, pady=20)
        backbtn=Button(self,width=10,text='Back',bg='gray36',fg='lemon chiffon',command=lambda: passman.backToStart(controller))
        backbtn.grid(row=4, columnspan=2, pady=10)




class MainPage(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller=controller
        self.configure(bg='gray12')
        sf= tkFont.Font(family='Helvetica', size=10, weight='bold')

        listFrame=Frame(self)

        addapp=Frame(self)
        addapp.configure(bg='gray12')
        lbx = Listbox(listFrame, width=50, height=15, background="gray80", selectbackground="gray80", font=sf)
        sbr=Scrollbar(listFrame)

        appnamelbl=Label(addapp, text="App Name",bg='gray12', fg='lemon chiffon')
        appnamelbl.configure(font=('Calibri Light', 12))
        appnamelbl.grid(row=0, column=0, padx=10)

        newappname=Entry(addapp, width=30)
        newappname.config({'background': 'gray80'})
        newappname.grid(row=0, column=1, padx=10, pady=10)
        
        appuserlbl=Label(addapp, text="Username",bg='gray12', fg='lemon chiffon')
        appuserlbl.configure(font=('Calibri Light', 12))
        appuserlbl.grid(row=1, column=0, padx=10)

        newappuser=Entry(addapp, width=30)
        newappuser.config({'background': 'gray80'})
        newappuser.grid(row=1, column=1, padx=10, pady=10)
        
        apppasslbl=Label(addapp, text="Password",bg='gray12', fg='lemon chiffon')
        apppasslbl.configure(font=('Calibri Light', 12))
        apppasslbl.grid(row=2, column=0, padx=10)

        newapppass=Entry(addapp, width=30)
        newapppass.config({'background': 'gray80'})
        newapppass.grid(row=2, column=1, padx=10, pady=10)
        
        addbtn=Button(addapp, width=20, text="Add App", bg='gray36',fg='lemon chiffon',command=lambda: passman.addApp(newappname, newappuser, newapppass))
        addbtn.configure(font=('Calibri Light', 10))
        
        addbtn.grid(row=3, column=0, padx=10, pady=10, columnspan=2)
        logoutbtn=Button(addapp,width=10,text='Logout',bg='gray36',fg='lemon chiffon',command=lambda: passman.logout(controller))
        logoutbtn.grid(row=4, column=0, padx=10, pady=5, columnspan=2)

        addapp.pack(side=RIGHT)
        sbr.pack(side=RIGHT, fill="y")
        sbr.config(command=lbx.yview)
        lbx.config(yscrollcommand=sbr.set)
        

        
        refreshbtn=Button(self,width=20,text='Refresh',bg='gray36',fg='lemon chiffon',command=lambda: passman.display(listFrame, lbx))
        refreshbtn.configure(font=('Calibri Light', 10))
        refreshbtn.pack(pady=10)




app = SampleApp()
app.configure(bg='gray12')
app.mainloop()