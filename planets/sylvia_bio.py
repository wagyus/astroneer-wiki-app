__author__ = 'chrismelnyk'
import tkinter as tk
from PIL import ImageTk,Image

root = tk.Tk()
root.geometry('400x725')
root.title('Sylvia Bio')

icon_img = 'images/icon_astro.jpg'
icon = ImageTk.PhotoImage(Image.open(icon_img))
root.tk.call('wm','iconphoto', root._w, icon)

img_planet = "images/planets/planet.icon/sylvia.icon.png"
img_1 = ImageTk.PhotoImage(Image.open(img_planet))

imgSyl = tk.Label(root, image=img_1, width=100, height=100)
imgSyl.pack()

textSyl = tk.Label(root, text="Sylvia is the first planet an adventurer will explore.\n\nIt's terrain is easy to traverse on foot and on vehicles.\n\nThe planets gives medium wind power and medium solar power.\n\nIt provides a wide amount of resources with large \ndeposits of compound, resin and graphite appearing on its surface.\nAnd in mountainous areas, malachite can be found in small amounts\n\nOn the planet's surface, there are 6 total Portals needing\nto be linked together. Around 8 small gerneraters are\nneeded to power each portal to full. With the Core Portal\nneeding Quartz to get the Geometric Triptych.\n")
textSyl.pack()

img = 'images/planets/planet.space/sylvia.space.png'
planet = ImageTk.PhotoImage(Image.open(img))

imageSly = tk.Label(root, image=planet)
imageSly.pack()

root.mainloop()