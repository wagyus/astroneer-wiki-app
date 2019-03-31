import tkinter as tk
from PIL import ImageTk,Image

root = tk.Tk()
root.title('Sylvia Planet View')
l1 = tk.Label(text="Sylvia Planet Info", fg="black", bg="snow")

img = 'images/planets/planet.space/sylvia.space.png'

sylvia_planet = ImageTk.PhotoImage(Image.open(img))

imageSly = tk.Label(root, image=sylvia_planet)
imageSly.pack()

root.mainloop()