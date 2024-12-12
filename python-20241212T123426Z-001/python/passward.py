from tkinter import *
import string
import random
import pyperclip
def generator():
    capital_letters=string.ascii_uppercase
    numbers=string.digits
    small_letters=string.ascii_lowercase
    spl_charecters=string.punctuation
    all=small_letters+capital_letters+numbers+spl_charecters+numbers
    password_length=int(lBox.get())
    if choice.get()==1:
        pField.insert(0,random.sample(small_letters+numbers,password_length))
    if choice.get()==2:
        pField.insert(0,random.sample(small_letters+numbers+capital_letters,password_length))
    if choice.get()==3:
        pField.insert(0,random.sample(all,password_length))
def copy():
    random_password=pField.get()
    pyperclip.copy(random_password)
password=Tk()
password.geometry("250x400")
password.title("Password Generator")
password.wm_iconbitmap("pword.ico")
choice=IntVar()
Font=('arial',13,'bold')
passwordLabel=Label(password,text='Password Generator',font=('times new roman',20,'bold'),bg='gray20',fg='white')
passwordLabel.grid(pady=10)
weak=Radiobutton(password,text='Weak',value=1,variable=choice,font=Font)
weak.grid(pady=5)
medium=Radiobutton(password,text='Medium',value=2,variable=choice,font=Font)
medium.grid(pady=5)
strong=Radiobutton(password,text='Strong',value=3,variable=choice,font=Font)
strong.grid(pady=5)
length=Label(password,text='Password Length',font=Font,bg='gray20',fg='white')
length.grid(pady=5)
lBox=Spinbox(password,from_=8,to_=18,width=5,font=Font)
lBox.grid(pady=5)
generateButton=Button(password,text='Generate',font=Font,command=generator)
generateButton.grid(pady=5)
pField=Entry(password,width=25,bd=2,font=Font)
pField.grid()
copyButton=Button(password,text='Copy',font=Font,command=copy)
copyButton.grid(pady=5)
password.mainloop()

