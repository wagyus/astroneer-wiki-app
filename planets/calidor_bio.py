__author__ = 'chrismelnyk and joelboder'
import tkinter as tk
from PIL import ImageTk,Image

root = tk.Tk()
root.geometry('400x725')
root.title('Atrox Bio')

icon_img = 'images/icon_astro.jpg'
icon = ImageTk.PhotoImage(Image.open(icon_img))
root.tk.call('wm','iconphoto', root._w, icon)

img_planet = "images/planets/planet.icon/atrox.icon.png"
img_1 = ImageTk.PhotoImage(Image.open(img_planet))

imgSyl = tk.Label(root, image=img_1, width=100, height=100)
imgSyl.pack()

textSyl = tk.Label(root, text="Atrox is the last planet in the solar system.\n\nIt's terrain is treacherous,\ndue to the rough surface and very aggressive flora.\n\nThe planets gives little wind and solar power.\n\nThe planet is void of any special ore, but the best source\n of Methane, Nitrogen, and Sulfur. While being the only source of Helium.\n\nOn the planet's surface, there are 6 total Portals needing\nto be linked together. With the Core Portal\nneeding Hydrogen to get the Geometric Triptych.\n")
textSyl.pack()

img = 'images/planets/planet.space/atrox.space.png'
planet = ImageTk.PhotoImage(Image.open(img))

imageSly = tk.Label(root, image=planet)
imageSly.pack()

root.mainloop()