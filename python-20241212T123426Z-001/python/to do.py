""" #uploading an image
from tkinter import *
from PIL import Image,ImageTk
p=Tk()
p.geometry("1200x1299")
niki=PhotoImage(file = "1.png")
#nikki=Image.open("nikki2.jpg")
#niki=ImageTk.PhotoImage(nikki)
nikitha=Button(image=niki)
nikitha.pack()
p.mainloop()
 """



# making an login page using label and button
# from tkinter import *
# r=Tk()
# def getval():
#     print("SuccessfullyCubmitted",uservalue.get(),passvalue.get())
#     with open("1.txt","a") as f:
#         f.write(f"{uservalue.get(),passvalue.get()}/n")
# r.geometry("542x742")
# Label(r,text="Welcome to login page").grid(row=0,column=4)
# username=Label(r,text="username")
# password=Label(r,text="password")
# username.grid(row=1,column=2)
# password.grid(row=2,column=2)
# uservalue=StringVar()
# passvalue=StringVar()
# userentry=Entry(r,textvariable=uservalue)
# passentry=Entry(r,textvariable=passvalue)
# userentry.grid(row=1,column=3)
# passentry.grid(row=2,column=3)
# submit=Button(r,text="Submit",command=getval).grid(row=3,column=3)
# r.mainloop()

""" import pickle
import tkinter as tk
from tkinter import messagebox

list = tk.Tk()
list.title("Creating List")
list.geometry("600x100")

def add():
    task = entry_task.get()
    if task != "":
        listbox_tasks.insert(tk.END, task)
        entry_task.delete(0,tk.END)
    else:
        messagebox.showwarning(title="Warning!", message="You have to enter a word.")

def delete():
    try:
        task_index = listbox_tasks.curselection()[0]
        listbox_tasks.delete(task_index)
    except IndexError:
        messagebox.showwarning(title="Warning!", message="You have to select a word.")

def update():
    try:
        task_index = listbox_tasks.curselection()[0]
        updated_task = entry_task.get()
        if updated_task != "":
            listbox_tasks.delete(task_index)
            listbox_tasks.insert(task_index, updated_task)
            entry_task.delete(0, tk.END)
        else:
            messagebox.showwarning(title="Warning!", message="You have to type in the yellow bar.")
    except IndexError:
        messagebox.showwarning(title="Warning!", message="You must select a word.")

# def load_tasks():
#     try:
#         tasks = pickle.load(open("tasks.dat", "rb"))
#         listbox_tasks.delete(0, tk.END)
#         for task in tasks:
#             listbox_tasks.insert(tk.END, task)
#     except FileNotFoundError:
#         messagebox.showwarning(title="Warning!", message="Cannot find tasks.dat.")

# def save_tasks():
#     tasks = list(listbox_tasks.get(0, tk.END))
#     pickle.dump(tasks, open("tasks.dat", "wb"))

listbox_tasks = tk.Listbox(list, height=10, width=50, bg="red", fg="white")
listbox_tasks.pack(side=tk.LEFT)

scrollbar_tasks = tk.Scrollbar(list)
scrollbar_tasks.pack(side=tk.RIGHT)

listbox_tasks.config(yscrollcommand=scrollbar_tasks.set)
scrollbar_tasks.config(command=listbox_tasks.yview)

entry_task = tk.Entry(list, width=50, bg="yellow")
entry_task.pack()

Add_task = tk.Button(list, text="Add", width=48, command=add, bg="blue")
Add_task.pack()

Delete_task = tk.Button(list, text="Delete", width=48, command=delete, bg="blue")
Delete_task.pack()

Update_task = tk.Button(list, text="Update", width=48, command=update, bg="grey", fg="white")
Update_task.pack()

# button_load_tasks = tk.Button(list, text="Load tasks", width=48, command=load_tasks)
# button_load_tasks.pack()

# button_save_tasks = tk.Button(list, text="Save tasks", width=48, command=save_tasks)
# button_save_tasks.pack()

list.mainloop()
 """


""" 
from tkinter import *
news=Tk()
def py():
    print("its cool")
lab=Label(news,text="dhgjnmjkhhb")
lab.pack()
can=PhotoImage(file="1.png")
pho=Button(image=can,command=py)
pho.pack()
news.mainloop()
 """



""" import tkinter as tk
import random

def play(player_choice):
    choices = ["Rock", "Paper", "Scissors"]
    computer_choice = random.choice(choices)
    result_text.set(f"Computer chose {computer_choice}\n")
    
    if player_choice == computer_choice:
        result_text.set(result_text.get() + "It's a tie!")
    elif (
        (player_choice == "Rock" and computer_choice == "Scissors") or
        (player_choice == "Paper" and computer_choice == "Rock") or
        (player_choice == "Scissors" and computer_choice == "Paper")
    ):
        result_text.set(result_text.get() + "You win!")
    else:
        result_text.set(result_text.get() + "You lose!")

# Create the main window
root = tk.Tk()
root.title("Rock Paper Scissors Game")
root.geometry("424x134")

# Create GUI elements
label = tk.Label(root, text="Select your choice:")
label.pack()

choices = ["Rock", "Paper", "Scissors"]
choice_var = tk.StringVar()
choice_var.set("Rock")
choice_menu = tk.OptionMenu(root, choice_var, *choices)
choice_menu.pack()

play_button = tk.Button(root, text="Play", command=lambda: play(choice_var.get()))
play_button.pack()

result_text = tk.StringVar()
result_label = tk.Label(root, textvariable=result_text)
result_label.pack()

# Start the GUI main loop
root.mainloop()
 """

""" 

import tkinter as tk
from tkinter import messagebox
import random

# Function to determine the winner
def determine_winner(user_choice):
    choices = ["Rock", "Paper", "Scissors"]
    computer_choice = random.choice(choices)
    
    if user_choice == computer_choice:
        result = "It's a tie!"
    elif (user_choice == "Rock" and computer_choice == "Scissors") or \
         (user_choice == "Paper" and computer_choice == "Rock") or \
         (user_choice == "Scissors" and computer_choice == "Paper"):
        result = "You win!"
    else:
        result = "Computer wins!"
    
    messagebox.showinfo("Result", f"Your choice: {user_choice}\nComputer's choice: {computer_choice}\nResult: {result}")

# Create the main window
root = tk.Tk()
root.title("Rock Paper Scissors Game")

# Create labels and buttons
label = tk.Label(root, text="Select your choice:")
label.pack()

choices = ["Rock", "Paper", "Scissors"]
for choice in choices:
    button = tk.Button(root, text=choice, command=lambda c=choice: determine_winner(c))
    button.pack()

# Start the GUI main loop
root.mainloop()
 """


# from tkinter import *
# r=Tk()
# r.geometry("242x343")
# r.wm_iconbitmap("2.ico")
# r.configure()
# r.mainloop()

""" 
from tkinter import *
import random

def start(user_choice):
    choices = ["Rock", "Paper", "Scissor"]
    computer = random.choice(choices)
    result.set(f"Computer chose {computer}\n")
    if computer == user_choice:
        result.set(result.get() + "It's a tie match")
    else:
        if (computer == "Rock" and user_choice == "Scissor") or \
           (computer == "Scissor" and user_choice == "Paper") or \
           (computer == "Paper" and user_choice == "Rock"):
            result.set(result.get() + "Computer is the winner and He won the match.")
        else:
            result.set(result.get() + "User is the winner and You won the match.")

rps = Tk()
rps.title("Rock Paper Scissor Game")
rps.geometry("250x150")
choices = ["Rock", "Paper", "Scissor"]
label=Label(text="Press the below Buttons to play the Game.",fg="red")
label.grid()
rock = Button(rps, text="Rock", command=lambda: start("Rock"))
rock.grid(row=1, column=0)
paper = Button(rps, text="Paper", command=lambda: start("Paper"))
paper.grid(row=1, column=1)
scissor = Button(rps, text="Scissor", command=lambda: start("Scissor"))
scissor.grid(row=1, column=2)
result = StringVar()
result.set("")
result_label = Label(rps, textvariable=result)
result_label.grid(row=4)
rps.mainloop() 
 """



from tkinter import *
import string
import random
import pyperclip

def generator():
    capital_letters = string.ascii_uppercase
    numbers = string.digits
    small_letters = string.ascii_lowercase
    spl_characters = string.punctuation
    all_characters = small_letters + capital_letters + numbers + spl_characters
    password_length = int(lBox.get())
    
    if choice.get() == 1:
        random_password = ''.join(random.choices(small_letters, k=password_length))
    elif choice.get() == 2:
        random_password = ''.join(random.choices(small_letters + capital_letters, k=password_length))
    elif choice.get() == 3:
        random_password = ''.join(random.choices(all_characters, k=password_length))
    
    pField.delete(0, END)  # Clear the entry field
    pField.insert(0, random_password)

def copy():
    random_password = pField.get()
    pyperclip.copy(random_password)

password = Tk()
password.geometry("250x400")
password.config(bg='yellow')
choice = IntVar()
Font = ('arial', 13, 'bold')

passwordLabel = Label(password, text='Password Generator', font=('times new roman', 20, 'bold'), bg='gray20', fg='white')
passwordLabel.grid(pady=10)

weak = Button(password, text='Weak', value=1, variable=choice, font=Font)
weak.grid(pady=5)

medium = Button(password, text='Medium', value=2, variable=choice, font=Font)
medium.grid(pady=5)

strong = Button(password, text='Strong', value=3, variable=choice, font=Font)
strong.grid(pady=5)

length = Label(password, text='Password Length', font=Font, bg='gray20', fg='white')
length.grid(pady=5)

lBox = Spinbox(password, from_=8, to_=18, width=5, font=Font)
lBox.grid(pady=5)

generateButton = Button(password, text='Generate', font=Font, command=generator)
generateButton.grid(pady=5)

pField = Entry(password, width=25, bd=2, font=Font)
pField.grid()

copyButton = Button(password, text='Copy', font=Font, command=copy)
copyButton.grid(pady=5)

password.mainloop()
