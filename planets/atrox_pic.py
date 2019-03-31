import tkinter as tk
from PIL import ImageTk,Image

root = tk.Tk()
root.title('Atrox Planet View')
l1 = tk.Label(text="Atrox Planet Info", fg="black", bg="snow")

img = 'images/planets/planet.space/atrox.space.png'

atrox_planet = ImageTk.PhotoImage(Image.open(img))

imageSly = tk.Label(root, image=atrox_planet)
imageSly.pack()

root.mainloop()