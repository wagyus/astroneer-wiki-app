__author__ = 'chrismelnyk'
import tkinter as tk
from PIL import ImageTk,Image
from subprocess import call

sylvia = 'planets/sylvia_info.py'
desolo = ''
calidor = ''
vesania = ''
novus = ''
glacio = ''
atrox = ''

def callpy1():
    call(['python', sylvia] )

def callpy2():
    call(['python', desolo])

def callpy3():
    call(['python', calidor])

def callpy4():
    call(['python', vesania])

def callpy5():
    call(['python', novus])

def callpy6():
    call(['python', glacio])

def callpy7():
    call(['python', atrox])

root = tk.Tk()
secondLevel = tk.Frame(master=root).grid(row=0, column=0)
root.geometry('100x400')
root.title('Astroneer Wiki')
l1 = tk.Label(text="Astroneer Wiki", fg="black", bg="white")

'''
Set image paths
'''


img_sylvia = "images/planets/planet.icon/sylvia.icon.png"
img_desolo = "images/planets/planet.icon/desolo.icon.png"
img_calidor = "images/planets/planet.icon/calidor.icon.png"
img_vesania = "images/planets/planet.icon/vesania.icon.png"
img_novus = "images/planets/planet.icon/novus.icon.png"
img_glacio = "images/planets/planet.icon/glacio.icon.png"
img_atro = "images/planets/planet.icon/atrox.icon.png"

'''
Import images using ImageTk
'''

img_1 = ImageTk.PhotoImage(Image.open(img_sylvia))
img_2 = ImageTk.PhotoImage(Image.open(img_desolo))
img_3 = ImageTk.PhotoImage(Image.open(img_calidor))
img_4 = ImageTk.PhotoImage(Image.open(img_vesania))
img_5 = ImageTk.PhotoImage(Image.open(img_novus))
img_6 = ImageTk.PhotoImage(Image.open(img_glacio))
img_7 = ImageTk.PhotoImage(Image.open(img_atro))

'''
Set images into GUI
'''

image1 = tk.Label(secondLevel, image = img_1, height=50, width=50).grid(row=0, column=0)
image2 = tk.Label(secondLevel, image = img_2, height=50, width=50).grid(row=1, column=0)
image3 = tk.Label(secondLevel, image = img_3, height=50, width=50).grid(row=2, column=0)
image4 = tk.Label(secondLevel, image = img_4, height=50, width=50).grid(row=3, column=0)
image5 = tk.Label(secondLevel, image = img_5, height=50, width=50).grid(row=4, column=0)
image6 = tk.Label(secondLevel, image = img_6, height=50, width=50).grid(row=5, column=0)
image7 = tk.Label(secondLevel, image = img_7, height=50, width=50).grid(row=6, column=0)

'''
Create buttons
'''

b1 = tk.Button(root, text='Sylvia', command=callpy1, height=2, width=5).grid(row=0, column=1)
b2 = tk.Button(root, text='Desolo', command=callpy2, height=2, width=5).grid(row=1, column=1)
b3 = tk.Button(root, text='Calidor', command=callpy3, height=2, width=5).grid(row=2, column=1)
b4 = tk.Button(root, text='Vesania', command=callpy4, height=2, width=5).grid(row=3, column=1)
b5 = tk.Button(root, text='Novus', command=callpy4, height=2, width=5).grid(row=4, column=1)
b6 = tk.Button(root, text='Glacio', command=callpy4, height=2, width=5).grid(row=5, column=1)
b7 = tk.Button(root, text='Atrox', command=callpy4, height=2, width=5).grid(row=6, column=1)

root.mainloop()