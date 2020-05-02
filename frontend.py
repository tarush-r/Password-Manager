import random
from tkinter import *
from tkinter.ttk import Combobox

  
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
  
  
root = Tk() 
frame=Frame(root)
root.title("Random Password Generator") 
var = IntVar() 
var1 = IntVar() 
  

  
Random_password = Label(root, text="Password",bg='gray12', fg='lemon chiffon') 
Random_password.grid(row=0,column=0,padx=10,pady=5) 
entry = Entry(root) 
entry.grid(row=0, column=1,padx=10,pady=5) 
  
c_label = Label(root, text="Length",bg='gray12') 
c_label.grid(row=1,column=0,padx=10,pady=5) 
  


 
generate_button = Button(root, text="Generate", command=generate,bg='gray36',fg='lemon chiffon') 
generate_button.configure(font=('Calibri Light', 20))
generate_button.grid(row=1, column=2,columnspan=3,padx=10,pady=5) 
  
radio_low = Radiobutton(root, text="Low", variable=var, value=1) 
radio_low.grid(row=0, column=2, sticky='E',padx=10,pady=5) 
radio_middle = Radiobutton(root, text="Medium", variable=var, value=0) 
radio_middle.grid(row=0, column=3, sticky='E',padx=10,pady=5) 
radio_strong = Radiobutton(root, text="Strong", variable=var, value=3) 
radio_strong.grid(row=0, column=4, sticky='E',padx=10,pady=5) 
combo = Combobox(root, textvariable=var1,width=17) 
  
combo['values'] = (8, 9, 10, 11, 12, 13, 14, 15, 16, 
                   17, 18, 19, 20, 21, 22, 23, 24, 25, 
                   26, 27, 28, 29, 30, 31, 32, "Length") 
combo.current(0) 
combo.bind('<<ComboboxSelected>>') 
combo.grid(column=1, row=1,padx=10,pady=5) 
frame.configure(bg='gray12')
frame.grid() 

root.mainloop() 