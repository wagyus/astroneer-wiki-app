import tkinter as tk
from PIL import ImageTk,Image

root = tk.Tk()
root.title('Desolo Planet View')
l1 = tk.Label(text="Desolo Planet Info", fg="black", bg="snow")

img = 'images/planets/planet.space/desolo.space.png'

desolo_planet = ImageTk.PhotoImage(Image.open(img))

imageSly = tk.Label(root, image=desolo_planet)
imageSly.pack()

root.mainloop()