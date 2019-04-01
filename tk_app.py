__author__ = 'chrismelnyk'
import tkinter as tk
from subprocess import call
from PIL import ImageTk,Image

planets = 'planets.py'
item_list = 'item_list.py'
soil_calc = 'soil/interface.py'
intake = ''

def callpy1():
    call(['python', planets] )

def callpy2():
    call(['python', item_list])

def callpy3():
    call(['python', soil_calc])

def callpy4():
    call(['python', intake])

root = tk.Tk()

icon_img = 'images/icon_astro.jpg'
icon = ImageTk.PhotoImage(Image.open(icon_img))
root.tk.call('wm','iconphoto', root._w, icon)

root.geometry('400x400')
root.title('Astroneer Wiki')
l1 = tk.Label(text="Astroneer Wiki", fg="black", bg="white")

b1 = tk.Button(root, text='Planets', command=callpy1, height=6, width=57).grid(row=0, column=1)
b2 = tk.Button(root, text='Item List', command=callpy2, height=6, width=57).grid(row=1, column=1)
b3 = tk.Button(root, text='', command=callpy3, height=6, width=57).grid(row=2, column=1)
b4 = tk.Button(root, text='', command=callpy4, height=6, width=57).grid(row=3, column=1)


root.mainloop()