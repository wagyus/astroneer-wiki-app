import tkinter as tk
from PIL import ImageTk,Image

root = tk.Tk()
root.title('Vesania Planet View')
l1 = tk.Label(text="Vesania Planet Info", fg="black", bg="snow")

img = 'images/planets/planet.space/vesania.space.png'

vesania_planet = ImageTk.PhotoImage(Image.open(img))

imageSly = tk.Label(root, image=vesania_planet)
imageSly.pack()

root.mainloop()