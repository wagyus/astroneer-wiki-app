__author__ = 'chrismelnyk and joelboder'
import tkinter as tk
from PIL import ImageTk,Image

root = tk.Tk()
root.geometry('500x625')
root.title('Novus Bio')

icon_img = 'images/icon_astro.jpg'
icon = ImageTk.PhotoImage(Image.open(icon_img))
root.tk.call('wm','iconphoto', root._w, icon)

img_planet = "images/planets/planet.icon/novus.icon.png"
img_1 = ImageTk.PhotoImage(Image.open(img_planet))

imgSyl = tk.Label(root, image=img_1, width=100, height=100)
imgSyl.pack()

textSyl = tk.Label(root, text="Novus is the moon of Vesania. It's surface is roughly the same as Desolo's.\n\nNovus gives high sun and wind power making it a good place for a second base.\n\nThere are 2 Gateway Chambers and 1 Silicone is required to activate the Geometric Triptych.")
textSyl.pack()

img = 'images/planets/planet.space/novus.space.png'
planet = ImageTk.PhotoImage(Image.open(img))

imageSly = tk.Label(root, image=planet)
imageSly.pack()

root.mainloop()