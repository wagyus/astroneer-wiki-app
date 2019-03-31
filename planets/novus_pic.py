import tkinter as tk
from PIL import ImageTk,Image

root = tk.Tk()
root.title('Novus Planet View')
l1 = tk.Label(text="Novus Planet Info", fg="black", bg="snow")

img = 'images/planets/planet.space/novus.space.png'

novus_planet = ImageTk.PhotoImage(Image.open(img))

imageSly = tk.Label(root, image=novus_planet)
imageSly.pack()

root.mainloop()