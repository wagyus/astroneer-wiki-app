__author__ = 'chrismelnyk and joelboder'
import tkinter as tk
from PIL import ImageTk,Image

root = tk.Tk()
root.geometry('400x675')
root.title('Vesania Bio')

icon_img = 'images/icon_astro.jpg'
icon = ImageTk.PhotoImage(Image.open(icon_img))
root.tk.call('wm','iconphoto', root._w, icon)

img_planet = "images/planets/planet.icon/vesania.icon.png"
img_1 = ImageTk.PhotoImage(Image.open(img_planet))

imgSyl = tk.Label(root, image=img_1, width=100, height=100)
imgSyl.pack()

textSyl = tk.Label(root, text="Vesania is the forth planet in the solar system.\n\nIt's surface is very unusual with a lush atmosphere\n\nThe planet gives very low sun and high \nwinds perfect for wind generators.\n\nThe primary resource is Lithium with Titanite as its secondary.\nHydrogen, Argon, and Nitrogen are the gasses avalible to get here.\n\nThe planet has 6 portal like the majority.\nThe core portal requires Graphene to unlock")
textSyl.pack()

img = 'images/planets/planet.space/vesania.space.png'
planet = ImageTk.PhotoImage(Image.open(img))

imageSly = tk.Label(root, image=planet)
imageSly.pack()

root.mainloop()