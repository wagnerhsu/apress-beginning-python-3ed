from tkinter import *
from tkinter import messagebox
from tkinter.scrolledtext import ScrolledText

top = Tk()
top.title("Simple Layout")

def command1():
    # Show a message box
    messagebox.showinfo("Message", "I'm in the first window!")
Button(text="TestButton", command=command1).pack()
mainloop()