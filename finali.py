from tkinter import *
from tkinter import ttk

win = Tk()
win.geometry("300x200")


def calc():
    inp = int(inp_text.get())
    summ = 0
    for i in range(1, inp):
        if inp % i == 0:
            summ += i
    if summ == inp:
        result.insert(0.0, f'{inp} is a Perfect Number')
    else:
        result.insert(0.0, f'{inp} is not a Perfect Number')


ttk.Label(win, text="შეიყვანეთ რიცხვი:").grid(row=1, sticky=W, pady=5, padx=10)

inp_text = ttk.Entry(win, width=20)
inp_text.grid(row=2, sticky="W", padx=10)

ttk.Button(win, text="გამოთვლა", command=calc).grid(row=2, column=1)

ttk.Label(win, text="სრულყოფილი რიცხვებია:").grid(row=3, sticky=W, pady=5, padx=10)

result = Text(win, width=30, height=5)
result.grid(row=4, column=0, columnspan=2, padx=10)

win.mainloop()
