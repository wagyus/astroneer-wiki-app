import tkinter as tk
from PIL import ImageTk,Image

root = tk.Tk()
root.title('Glacio Planet View')
l1 = tk.Label(text="Glacio Planet Info", fg="black", bg="snow")

img = 'images/planets/planet.space/glacio.space.png'

glacio_planet = ImageTk.PhotoImage(Image.open(img))

imageSly = tk.Label(root, image=glacio_planet)
imageSly.pack()

root.mainloop()