from tkinter import *
def press(num):
    global text
    text = text + str(num)
    equation.set(text)
def equal():
    global text
    try:
        t = str(eval(text))
        equation.set(t)
        text = t
    except SyntaxError:
        equation.set("syntax error")
        text = ""
    except ZeroDivisionError:
        equation.set("arithmetic error")
        text = ""
def clear():
    global text
    equation.set("")
    text = ""
calculator = Tk()
calculator.title("Calculator")
calculator.geometry("400x500")
text = ""
equation= StringVar()
label = Label(calculator, textvariable=equation, font=('Helvetica',20),bg="white", width=23, height=2)
label.pack()
frame = Frame(calculator)
frame.pack()
a = Button(frame, text=1, height=3, width=7, font=35, command=lambda: press(1),bg="black",fg="white")
a.grid(row=0, column=0)
b = Button(frame, text=2, height=3, width=7, font=35, command=lambda: press(2),bg="black",fg="white")
b.grid(row=0, column=1)
c = Button(frame, text=3, height=3, width=7, font=35, command=lambda: press(3),bg="black",fg="white")
c.grid(row=0, column=2)
d = Button(frame, text=4, height=3, width=7, font=35, command=lambda: press(4),bg="black",fg="white")
d.grid(row=1, column=0)
e = Button(frame, text=5, height=3, width=7, font=35, command=lambda: press(5),bg="black",fg="white")
e.grid(row=1, column=1)
f = Button(frame, text=6, height=3, width=7, font=35, command=lambda: press(6),bg="black",fg="white")
f.grid(row=1, column=2)
i = Button(frame, text=7, height=3, width=7, font=35, command=lambda: press(7),bg="black",fg="white")
i.grid(row=2, column=0)
j = Button(frame, text=8, height=3, width=7, font=35, command=lambda: press(8),bg="black",fg="white")
j.grid(row=2, column=1)
h = Button(frame, text=9, height=3, width=7, font=35, command=lambda: press(9),bg="black",fg="white")
h.grid(row=2, column=2)
g = Button(frame, text=0, height=3, width=7, font=35, command=lambda: press(0),bg="black",fg="white")
g.grid(row=3, column=0)
p = Button(frame, text='+', height=3, width=7, font=35, command=lambda: press('+'),bg="black",fg="white")
p.grid(row=0, column=3)
mi = Button(frame, text='-', height=3, width=7, font=35, command=lambda: press('-'),bg="black",fg="white")
mi.grid(row=1, column=3)
mu = Button(frame, text='*', height=3, width=7, font=35, command=lambda: press('*'),bg="black",fg="white")
mu.grid(row=2, column=3)
di = Button(frame, text='/', height=3, width=7, font=35, command=lambda: press('/'),bg="black",fg="white")
di.grid(row=3, column=3)
equ = Button(frame, text='=', height=3, width=7, font=35, command=equal,bg="black",fg="white")
equ.grid(row=3, column=2)
dec = Button(frame, text='.', height=3, width=7, font=35, command=lambda: press('.'),bg="black",fg="white")
dec.grid(row=3, column=1)
clear = Button(calculator, text='clear', height=2, width=10, font=35, command=clear,bg="black",fg="white")
clear.pack()
calculator.mainloop()

