from tkinter import * 
from tkinter import messagebox
import random

def start(user_choice):
    choices = ["Rock", "Paper", "Scissor"]
    AI = random.choice(choices)
    result.set(f"Computer chose {AI}\n")
    if AI == user_choice:
        messagebox.showwarning( message=result.get() + "Its a tie match.")
    else:
        if (AI == "Rock" and user_choice == "Scissor") or \
           (AI== "Scissor" and user_choice == "Paper") or \
           (AI == "Paper" and user_choice == "Rock"):
            messagebox.showwarning(title="AI is the winner", message=result.get() + "Computer is the winner and He won the match.")
        else:
            messagebox.showwarning(title="You are the winner", message=result.get()+"User is the winner and You won the match.")

rps = Tk()
rps.title("Rock Paper Scissor Game")
rps.geometry("250x1000")
choices = ["Rock", "Paper", "Scissor"]
label=Label(text="Press the below Buttons to play the Game.",fg="red")
label.grid()
r=PhotoImage(file = "r.png")
p=PhotoImage(file = "p.png")
s=PhotoImage(file = "s.png")
rock = Button(rps, image=r, command=lambda: start("Rock"))
rock.grid(row=1, column=0,pady=10)
paper = Button(rps, image=p, command=lambda: start("Paper"))
paper.grid(row=2, column=0,pady=10)
scissor = Button(rps, image=s, command=lambda: start("Scissor"))
scissor.grid(row=3, column=0,pady=10)
result = StringVar()
result.set("")
result_label = Label(rps, textvariable=result)
result_label.grid(row=4)
rps.mainloop()