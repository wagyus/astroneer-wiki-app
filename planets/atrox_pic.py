import tkinter as tk
from PIL import ImageTk,Image

root = tk.Tk()
root.title('Atrox Planet View')
l1 = tk.Label(text="Atrox Planet Info", fg="black", bg="snow")

icon_img = 'images/icon_astro.jpg'
icon = ImageTk.PhotoImage(Image.open(icon_img))
root.tk.call('wm','iconphoto', root._w, icon)

img = 'images/planets/planet.space/atrox.space.png'

atrox_planet = ImageTk.PhotoImage(Image.open(img))

imageSly = tk.Label(root, image=atrox_planet)
imageSly.pack()

root.mainloop()