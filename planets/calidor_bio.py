__author__ = 'chrismelnyk and joelboder'
import tkinter as tk
from PIL import ImageTk,Image

root = tk.Tk()
root.geometry('400x725')
root.title('Calidor Bio')

icon_img = 'images/icon_astro.jpg'
icon = ImageTk.PhotoImage(Image.open(icon_img))
root.tk.call('wm','iconphoto', root._w, icon)

img_planet = "images/planets/planet.icon/calidor.icon.png"
img_1 = ImageTk.PhotoImage(Image.open(img_planet))

imgSyl = tk.Label(root, image=img_1, width=100, height=100)
imgSyl.pack()

textSyl = tk.Label(root, text="Calidor is the third planet in the solar system.\n\nIt's terrain is a mild, desert surface, with sand dunes and frequent canyons.\n\nThe planets gives little wind and high solar power.\n\nThe planet is a great source of Malachite and a good source of Wolframite.\nThere are two gasses that can be found here, Hydrogen and Sulfur.\n\nOn the planet's surface, there are 6 total Portals needing\nto be linked together. With the Core Portal\nneeding Explosive Powder to get the Geometric Triptych.\n")
textSyl.pack()

img = 'images/planets/planet.space/calidor.space.png'
planet = ImageTk.PhotoImage(Image.open(img))

imageSly = tk.Label(root, image=planet)
imageSly.pack()

root.mainloop()