#Calculator for soil centrifuge
#1. Select item from image
#2. Enter how many items you need
#3. Outputs the amount of dirt canisters you need
import tkinter as tk
from subprocess import call
from PIL import ImageTk,Image

compound = 'soil/compound.py'
resin = 'soil/resin.py'
ammonium = 'soil/ammonium.py'
clay = 'soil/clay.py'
organic = 'soil/organic.py'
quartz = 'soil/quartz.py'
graphite = 'soil/graphite.py'

def callcompound():
    call(['python', compound])

def callresin():
    call(['python', resin])

def callammonium():
    call(['python', ammonium])

def callclay():
    call(['python', clay])

def callorganic():
    call(['python', organic])

def callquartz():
    call(['python', quartz])

def callgraphite():
    call(['python', graphite])

root = tk.Tk()

icon_img = 'images/icon_astro.jpg'
icon = ImageTk.PhotoImage(Image.open(icon_img))
root.tk.call('wm','iconphoto', root._w, icon)

root.geometry('742x105')
root.title('Soil Centrifuge - Select a Resource')

img_comound = "images/resources/compound.png"
img_resin = "images/resources/resin.png"
img_organic = "images/resources/organic.png"
img_clay = "images/resources/clay.png"
img_graphite = "images/resources/graphite.png"
img_quartz = "images/resources/quartz.png"
img_ammonium = "images/resources/ammonium.png"

compound_icon = ImageTk.PhotoImage(Image.open(img_comound))
resin_icon = ImageTk.PhotoImage(Image.open(img_resin))
organic_icon = ImageTk.PhotoImage(Image.open(img_organic))
clay_icon = ImageTk.PhotoImage(Image.open(img_clay))
graphite_icon = ImageTk.PhotoImage(Image.open(img_graphite))
quartz_icon = ImageTk.PhotoImage(Image.open(img_quartz))
ammonium_icon = ImageTk.PhotoImage(Image.open(img_ammonium))

tk.Button(root, image=compound_icon, command=callcompound, width=100, height=100).grid(row=0, column=0)
tk.Button(root, image=resin_icon, command=callresin, width=100, height=100).grid(row=0, column=1)
tk.Button(root, image=organic_icon, command=callorganic, width=100, height=100).grid(row=0, column=2)
tk.Button(root, image=clay_icon, command=callclay, width=100, height=100).grid(row=0, column=3)
tk.Button(root, image=quartz_icon,command=callquartz, width=100, height=100).grid(row=0, column=4)
tk.Button(root, image=graphite_icon,command=callgraphite, width=100, height=100).grid(row=0, column=5)
tk.Button(root, image=ammonium_icon,command=callammonium, width=100, height=100).grid(row=0, column=6)

root.mainloop()
