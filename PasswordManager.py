from tkinter import *              
from tkinter import font  as tkFont 
import passman
# import tkFont
# from PyInstaller.utils.hooks import collect_data_files
# datas = collect_data_files('grpc')

class SampleApp(Tk):

    def __init__(self, *args, **kwargs):
        Tk.__init__(self, *args, **kwargs)
        
        self.geometry('800x450')
        self.minsize(800, 450)
        self.maxsize(800, 450)
        container = Frame(self)
        container.place(relx=0.5, rely=0.5, anchor=CENTER)

        self.frames = {}
        for F in (StartPage, LoginPage, RegisterPage, MainPage):
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
        # self.pack(expand=True)
        # self.place(relx=0.5, rely=0.5, anchor=CENTEsR)


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
# class LoginPage(Frame):
#     def __init__(self, parent, controller):
#         Frame.__init__(self, parent)
#         self.controller = controller
#         loginTitle=Label(self, text="Login").grid(row=0, column=0)
#         ginTitle=Label(self, text="Login").grid(row=1, column=0)
#         lonTitle=Label(self, text="Login").grid(row=2, column=0)
#         logiitle=Label(self, text="Login").grid(row=3, column=0)
#         oginTitle=Label(self, text="Login").grid(row=4, column=0)
#         loinTitle=Label(self, text="Login").grid(row=5, column=0)
#         logiTitle=Label(self, text="Login").grid(row=6, column=0)
#         loginTtle=Label(self, text="Login").grid(row=7, column=0)
#         loginTite=Label(self, text="Login").grid(row=8, column=0)
        

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
        
        # userlbl=Label(self,text='Username',bg='gray12').grid(row=1, column=0, pady=10, padx=10)
        # userfield=Entry(self, width=60)
        # userfield.grid(row=1, column=1, pady=10)

        # passlbl=Label(self,text='Password',bg='gray12').grid(row=2, column=0, pady=10, padx=10)
        # passfield=Entry(self,width=60)
        # passfield.grid(row=2, column=1, pady=10)
        passlbl=Label(self,text='Password',bg='gray12', fg='lemon chiffon')
        passlbl.configure(font=('Calibri Light', 12))
        passlbl.grid(row=2, column=0, pady=5, padx=20)
        passfield=Entry(self,width=40)
        passfield.config({'background': 'gray80'})
        passfield.grid(row=2, column=1, pady=10)



        registerbtn=Button(self,width=20,text='Login',bg='gray36',fg='lemon chiffon', command=lambda: passman.createUser(userfield, passfield, controller))
        registerbtn.configure(font=('Calibri Light', 10))
        registerbtn.grid(row=3, columnspan=2, pady=20)



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

        addapp.pack(side=RIGHT)
        sbr.pack(side=RIGHT, fill="y")
        sbr.config(command=lbx.yview)
        lbx.config(yscrollcommand=sbr.set)
        

        
        refreshbtn=Button(self,width=20,text='Refresh',bg='gray36',fg='lemon chiffon',command=lambda: passman.display(listFrame, lbx))
        refreshbtn.configure(font=('Calibri Light', 10))
        refreshbtn.pack(pady=10)

# class PageTwo(Frame):

#     def __init__(self, parent, controller):
#         tk.Frame.__init__(self, parent)
#         self.controller = controller
#         label = Label(self, text="This is page 2", font=controller.title_font)
#         label.pack(side="top", fill="x", pady=10)
#         button = Button(self, text="Go to the start page",
#                            command=lambda: controller.show_frame("StartPage"))
#         button.pack()



app = SampleApp()
app.configure(bg='gray12')
app.mainloop()