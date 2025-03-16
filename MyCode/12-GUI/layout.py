from tkinter import *
from tkinter.scrolledtext import ScrolledText

top = Tk()
top.title("Simple Layout")

Label(text="I'm in the first window!").pack()
second = Toplevel()
Label(second, text="I'm in the second window!").pack()
mainloop()