from tkinter import *
import random

root = Tk()
root.title('Multiplication Table')
root.grid_rowconfigure(0, minsize=33)
res = IntVar()


def calculate():
    x = var1.get()
    y = var2.get()
    res = int(x) * int(y)
    colour = "%06x" % random.randint(0,0xFFFFFF)
    colour = "#" + colour
    result.config(fg=colour)
    result.config(text=res)


num = [
    ('1','1'),
    ('2','2'),
    ('3','3'),
    ('4','4'),
    ('5','5'),
    ('6','6'),
    ('7','7'),
    ('8','8'),
    ('9','9'),
    ('10','10')]

var1 = StringVar()
var1.set("1")
var2 = StringVar()
var2.set("1")

col = 1
for text, val in num:
    r = Radiobutton(root, text = text, variable = var1, value = val, command=calculate)
    r.grid(row=0, column=col)
    col = col + 1
row = 1
for text, val in num:
    r = Radiobutton(root, text = text, variable = var2, value = val, command=calculate)
    r.grid(row=row, column=0)
    root.grid_rowconfigure(row, minsize=33)
    row = row + 1

result = Label(root, text = "1", fg="pink", font=("Arial", 70, "bold"))
result.grid(row = 4, column = 1, rowspan=3, columnspan=10)

root.mainloop()
