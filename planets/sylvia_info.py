import tkinter as tk
from PIL import ImageTk,Image

root = tk.Tk()
secondLevel = tk.Frame(master=root).grid(row=0, column=3)
root.geometry('500x500')
root.title('Astroneer Wiki')
l1 = tk.Label(text="Sylvia Planet Info", fg="black", bg="white")

img_icon = "images/planets/planet.icon/sylvia.icon.png"
img_planet = "images/planets/planet.space/sylvia.space.png"

sylvia_planet = ImageTk.PhotoImage(Image.open(img_planet))
sylvia_icon = ImageTk.PhotoImage(Image.open(img_icon))

#planetIcon = tk.Label(root, image = sylvia_icon, height=50, width=50).grid(row=0, column=0)
#planetImage = tk.Label(root, image = sylvia_planet, height=350, width=350, anchor="nw").grid(row=0, column=0)

#tk.Label(root, text="SYLVIA RESOURCES", font="Helvetica", justify="left").grid(row=3, column=0)

tk.Label(root, text="SYLVIA RESOURCES\n===================\nCompound\nResin\nOrganic\nClay\nGraphite\nQuartz\nLaterite\nAmmonium\nAstronium", font="Helvetica").grid(row=0, column=1)
'''
tk.Label(root, text="Compound", font="Helvetica", justify="left").grid(row=1, column=1)
tk.Label(root, text="Resin", font="Helvetica", justify="left").grid(row=2, column=1)
tk.Label(root, text="Organic", font="Helvetica", justify="left").grid(row=3, column=1)
tk.Label(root, text="Clay", font="Helvetica", justify="left").grid(row=4, column=1)
tk.Label(root, text="Graphite", font="Helvetica", justify="left").grid(row=5, column=1)
tk.Label(root, text="Quartz", font="Helvetica", justify="left").grid(row=6, column=1)
tk.Label(root, text="Laterite", font="Helvetica", justify="left").grid(row=7, column=1)
tk.Label(root, text="Ammonium", font="Helvetica", justify="left").grid(row=8, column=1)
tk.Label(root, text="Astronium", font="Helvetica", justify="left").grid(row=9, column=1)
'''


tk.Label(root, text="PRIMARY RESOURCES\n====================\nSphalerite", font="Helvetica").grid(row=0, column=2)
'''
tk.Label(root, text="===================", font="Helvetica").grid(row=1, column=2)
tk.Label(root, text="Resin", font="Helvetica").grid(row=2, column=2)
'''

'''
tk.Label(root, text="GASES", font="Helvetica").grid(row=0, column=3)
tk.Label(root, text="===================", font="Helvetica").grid(row=1, column=3)
'''
#tk.Label(root, text="Resin", font="Helvetica").grid(row=2, column=3)
#tk.Label(root, text="Resin", font="Helvetica").grid(row=3, column=3)

tk.Label(root, text="").grid(row=0, column=3)


root.mainloop()