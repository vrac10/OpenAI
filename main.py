import tkinter
from customtkinter import *
import Model

root = CTk()
textForGPT = ""
root.geometry('700x800')

text = CTkEntry(root)
text.grid(row = 1, column = 0)
def text_gen():
    a = text.get()
    final =  Model.generation(a)
    textForGPT = final
    label.configure(text = final)
    text.delete(0,END)
button = CTkButton(root, text= 'send', width = 50, command= text_gen)
button.grid(row = 1, column = 1)
label = CTkLabel(root, text = "Hi what can i do for you")
label.grid(row = 0, column = 0)
root.mainloop()
