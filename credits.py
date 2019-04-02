import tkinter as tk
from PIL import ImageTk,Image

root = tk.Tk()

icon_img = 'images/icon_astro.jpg'
icon = ImageTk.PhotoImage(Image.open(icon_img))
root.tk.call('wm','iconphoto', root._w, icon)

img_woomy = 'images/extra/Astro.woomy.png'
woomy = ImageTk.PhotoImage(Image.open(img_woomy))
root.geometry('600x500')
root.title('Astroneer Wiki')
l1 = tk.Label(text="Astroneer Wiki", fg="black", bg="white")

l2 = tk.Label(text="This was a project created in four days so there may be some errors throughout. \n\nProgramming: chrismelnyk\n\nPython Baby: playthetrack\n\nThanks for taking a look at this and feel free to add\nany issues and pull requests.")
l2.config(font=("Helvetica", 13))
l2.pack()

l3 = tk.Label(image=woomy)
l3.pack()

root.mainloop()