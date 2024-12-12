

import pickle
import tkinter as tk
from tkinter import Y,X, Label, messagebox,END
from tkinter.font import BOLD

list = tk.Tk()
list.title("Creating List")
list.geometry("600x120")

def add():
    task = entry.get()
    if task != "":
        listbox.insert(tk.END, task)
        entry.delete(0,tk.END)
    else:
        messagebox.showwarning(title="Warning!", message="You have to enter a word.")

def delete():
    try:
        task_index = listbox.curselection()[0]
        listbox.delete(task_index)
    except IndexError:
        messagebox.showwarning(title="Warning!", message="You have to select a word.")

def update():
    try:
        task_index = listbox.curselection()[0]
        updated_task = entry.get()
        if updated_task != "":
            listbox.delete(task_index)
            listbox.insert(task_index, updated_task)
            entry.delete(0, tk.END)
        else:
            messagebox.showwarning(title="Warning!", message="You have to type in the yellow bar.")
    except IndexError:
        messagebox.showwarning(title="Warning!", message="You must select a word.")

listbox= tk.Listbox(list, width=50, bg="red", fg="white")
listbox.pack(side=tk.LEFT,fill=tk.BOTH,padx=5)
l=Label(list,text="Enter the values here:",font=BOLD)
l.pack(fill=X)
list.wm_iconbitmap("list.ico")
listbox.insert(END)
scroll= tk.Scrollbar(list)
scroll.pack(side=tk.RIGHT,fill=Y)
listbox.config(yscrollcommand=scroll.set)
scroll.config(command=listbox.yview)
entry = tk.Entry(list, width=50, bg="yellow")
entry.pack(padx=5,fill=X)
Add= tk.Button(list, text="Add", width=48, command=add, bg="grey")
Add.pack(padx=5,fill=X)
Delete = tk.Button(list, text="Delete", width=48, command=delete, bg="grey")
Delete.pack(padx=5,fill=X)
Update = tk.Button(list, text="Edit", width=48, command=update, bg="grey")
Update.pack(padx=5,fill=X)
list.mainloop()