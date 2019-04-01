#INSERT ITEM LIST IN A GRID FORMAT
#ITEM ICON | ITEM NAME | SMELTED | ATHMOSPHERIC CONDENSOR | CHEM LAB USED IN

__author__ = 'chrismelnyk'
import tkinter as tk
from PIL import ImageTk,Image
from tkinter import font

root = tk.Tk()
root.geometry('600x670')
root.title('Item List')

icon_img = 'images/icon_astro.jpg'
icon = ImageTk.PhotoImage(Image.open(icon_img))
root.tk.call('wm','iconphoto', root._w, icon)
#ALL ITEMS BELOW
img_comound = "images/resources/compound.png"
img_resin = "images/resources/resin.png"
img_organic = "images/resources/organic.png"
img_clay = "images/resources/clay.png"
img_graphite = "images/resources/graphite.png"
img_quartz = "images/resources/quartz.png"
img_laterite = "images/resources/laterite.png"
img_sphalerite = "images/resources/sphalerite.png"
img_malachite = "images/resources/malachite.png"
img_wolframite = "images/resources/wolframite.png"
img_titanite = "images/resources/titanite.png"
img_hermatite = "images/resources/hematite.png"
img_ammonium = "images/resources/ammonium.png"
img_astronium = "images/resources/astronium.png"
img_lithium = "images/resources/lithium.png"

hermatite_icon = ImageTk.PhotoImage(Image.open(img_hermatite))
wolframite_icon = ImageTk.PhotoImage(Image.open(img_wolframite))
titanite_icon = ImageTk.PhotoImage(Image.open(img_titanite))
compound_icon = ImageTk.PhotoImage(Image.open(img_comound))
resin_icon = ImageTk.PhotoImage(Image.open(img_resin))
organic_icon = ImageTk.PhotoImage(Image.open(img_organic))
clay_icon = ImageTk.PhotoImage(Image.open(img_clay))
graphite_icon = ImageTk.PhotoImage(Image.open(img_graphite))
quartz_icon = ImageTk.PhotoImage(Image.open(img_quartz))
laterite_icon = ImageTk.PhotoImage(Image.open(img_laterite))
ammonium_icon = ImageTk.PhotoImage(Image.open(img_ammonium))
astronium_icon = ImageTk.PhotoImage(Image.open(img_astronium))
sphalerite_icon = ImageTk.PhotoImage(Image.open(img_sphalerite))
malachite_icon = ImageTk.PhotoImage(Image.open(img_malachite))
lithium_icon = ImageTk.PhotoImage(Image.open(img_lithium))

tk.Label(root, text="ICON").grid(row=0, column=0,)
tk.Label(root, text="------------").grid(row=1, column=0,)
tk.Label(root, image=resin_icon, height=30, width=30).grid(row=2, column=0)
tk.Label(root, image=quartz_icon, height=30, width=30).grid(row=3, column=0)
tk.Label(root, image=compound_icon, height=30, width=30).grid(row=4, column=0)
tk.Label(root, image=organic_icon, height=30, width=30).grid(row=5, column=0)
tk.Label(root, image=wolframite_icon, height=30, width=30).grid(row=6, column=0)
tk.Label(root, image=clay_icon, height=30, width=30).grid(row=7, column=0)
tk.Label(root, image=hermatite_icon, height=30, width=30).grid(row=8, column=0)
tk.Label(root, image=malachite_icon, height=30, width=30).grid(row=9, column=0)
tk.Label(root, image=laterite_icon, height=30, width=30).grid(row=10, column=0)
tk.Label(root, image=ammonium_icon, height=30, width=30).grid(row=11, column=0)
tk.Label(root, image=graphite_icon, height=30, width=30).grid(row=12, column=0)
tk.Label(root, image=titanite_icon, height=30, width=30).grid(row=13, column=0)
tk.Label(root, image=lithium_icon, height=30, width=30).grid(row=14, column=0)
tk.Label(root, image=astronium_icon, height=30, width=30).grid(row=15, column=0)
tk.Label(root, image=sphalerite_icon, height=30, width=30).grid(row=16, column=0)

root.mainloop()