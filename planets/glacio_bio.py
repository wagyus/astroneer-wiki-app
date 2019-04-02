__author__ = 'chrismelnyk and joelboder'
import tkinter as tk
from PIL import ImageTk,Image

root = tk.Tk()
root.geometry('400x650')
root.title('Glacio Bio')

icon_img = 'images/icon_astro.jpg'
icon = ImageTk.PhotoImage(Image.open(icon_img))
root.tk.call('wm','iconphoto', root._w, icon)

img_planet = "images/planets/planet.icon/glacio.icon.png"
img_1 = ImageTk.PhotoImage(Image.open(img_planet))

imgSyl = tk.Label(root, image=img_1, width=100, height=100)
imgSyl.pack()

textSyl = tk.Label(root, text="Glacio is the sixth planet in the solar system.\n\nIt's surface is windly and icy with mountanous regions.\n It's underground hosts Popcoral, Popper and Lobber plants.\n\nThe planet gives very low sun and extreme \nwinds making it perfect for wind generators.\n\nGlacio has 6 Gateway Chambers. The core is activated with 1 diamond.")
textSyl.pack()

img = 'images/planets/planet.space/glacio.space.png'
planet = ImageTk.PhotoImage(Image.open(img))

imageSly = tk.Label(root, image=planet)
imageSly.pack()

root.mainloop()