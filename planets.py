__author__ = 'chrismelnyk'
import tkinter as tk
from PIL import ImageTk,Image
from subprocess import call

sylvia = 'planets/sylvia_info.py'
sylvia_pic = 'planets/sylvia_pic.py'
sylvia_bio = 'planets/sylvia_bio.py'
desolo = 'planets/desolo_info.py'
desolo_pic = 'planets/desolo_pic.py'
desolo_bio = 'planets/desolo_bio.py'
calidor = 'planets/calidor_info.py'
calidor_pic = 'planets/calidor_pic.py'
calidor_bio = 'planets/calidor_bio.py'
vesania = 'planets/vesania_info.py'
vesania_pic = 'planets/vesania_pic.py'
vesania_bio = 'planets/vesania_bio.py'
novus = 'planets/novus_info.py'
novus_pic = 'planets/novus_pic.py'
novus_bio = 'planets/novus_bio.py'
glacio = 'planets/glacio_info.py'
glacio_pic = 'planets/glacio_pic.py'
glacio_bio = 'planets/glacio_bio.py'
atrox = 'planets/atrox_info.py'
atrox_pic = 'planets/atrox_pic.py'
atrox_bio = 'planets/atrox_bio.py'

def callpy1():
    call(['python', sylvia])

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

def callsylvia_pic():
    call(['python', sylvia_pic])

def calldesolo_pic():
    call(['python', desolo_pic])

def callcalidor_pic():
    call(['python', calidor_pic])

def callvesania_pic():
    call(['python', vesania_pic])

def callnovus_pic():
    call(['python', novus_pic])

def callglacio_pic():
    call(['python', glacio_pic])

def callatrox_pic():
    call(['python', atrox_pic])

def callsylvia_bio():
    call(['python', sylvia_bio])

def callcalidor_bio():
    call(['python', calidor_bio])

def calldesolo_bio():
    call(['python', desolo_bio])

def callglacio_bio():
    call(['python', glacio_bio])

def callnovus_bio():
    call(['python', novus_bio])

def callvesania_bio():
    call(['python', vesania_bio])

def callatrox_bio():
    call(['python', atrox_bio])


root = tk.Tk()
root.geometry('400x400')
root.title('Planet Selection')
l1 = tk.Label(text="Astroneer Wiki", fg="black", bg="white")

icon_img = 'images/icon_astro.jpg'
icon = ImageTk.PhotoImage(Image.open(icon_img))
root.tk.call('wm','iconphoto', root._w, icon)

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
'''
image1 = tk.Label(secondLevel, image = img_1, height=50, width=50).grid(row=0, column=0)
image2 = tk.Label(secondLevel, image = img_2, height=50, width=50).grid(row=1, column=0)
image3 = tk.Label(secondLevel, image = img_3, height=50, width=50).grid(row=2, column=0)
image4 = tk.Label(secondLevel, image = img_4, height=50, width=50).grid(row=3, column=0)
image5 = tk.Label(secondLevel, image = img_5, height=50, width=50).grid(row=4, column=0)
image6 = tk.Label(secondLevel, image = img_6, height=50, width=50).grid(row=5, column=0)
image7 = tk.Label(secondLevel, image = img_7, height=50, width=50).grid(row=6, column=0)
'''
'''
Create buttons
'''

b1 = tk.Button(root, image = img_1, command=callsylvia_pic, height=50, width=50).grid(row=1, column=0)
b2 = tk.Button(root, image = img_2, command=calldesolo_pic, height=50, width=50).grid(row=2, column=0)
b3 = tk.Button(root, image = img_3, command=callcalidor_pic, height=50, width=50).grid(row=3, column=0)
b4 = tk.Button(root, image = img_4, command=callvesania_pic, height=50, width=50).grid(row=4, column=0)
b5 = tk.Button(root, image = img_5, command=callnovus_pic, height=50, width=50).grid(row=5, column=0)
b6 = tk.Button(root, image = img_6, command=callglacio_pic, height=50, width=50).grid(row=6, column=0)
b7 = tk.Button(root, image = img_7, command=callatrox_pic, height=50, width=50).grid(row=7, column=0)

b8 = tk.Button(root, text = 'Sylvia Resources', command=callpy1, height=3, width=20).grid(row=1, column=1)
b9 = tk.Button(root, text='Desolo Resources', command=callpy2, height=3, width=20).grid(row=2, column=1)
b10 = tk.Button(root, text='Calidor Resources', command=callpy3, height=3, width=20).grid(row=3, column=1)
b11 = tk.Button(root, text='Vesania Resources', command=callpy4, height=3, width=20).grid(row=4, column=1)
b12 = tk.Button(root, text='Novus Resources', command=callpy5, height=3, width=20).grid(row=5, column=1)
b13 = tk.Button(root, text='Glacio Resources', command=callpy6, height=3, width=20).grid(row=6, column=1)
b14 = tk.Button(root, text='Atrox Resources', command=callpy7, height=3, width=20).grid(row=7, column=1)

b15 = tk.Button(root, text = 'Bio', command=callsylvia_bio, height=3, width=20).grid(row=1, column=2)
b16 = tk.Button(root, text='Bio', command=calldesolo_bio, height=3, width=20).grid(row=2, column=2)
b17 = tk.Button(root, text='Bio', command=callcalidor_bio, height=3, width=20).grid(row=3, column=2)
b18 = tk.Button(root, text='Bio', command=callvesania_bio, height=3, width=20).grid(row=4, column=2)
b19 = tk.Button(root, text='Bio', command=callnovus_bio, height=3, width=20).grid(row=5, column=2)
b20 = tk.Button(root, text='Bio', command=callglacio_bio, height=3, width=20).grid(row=6, column=2)
b21 = tk.Button(root, text='Bio', command=callatrox_bio, height=3, width=20).grid(row=7, column=2)

root.mainloop()