#INSERT ITEM LIST IN A GRID FORMAT
#ITEM ICON | ITEM NAME | SMELTED | ATHMOSPHERIC CONDENSOR | CHEM LAB USED IN

__author__ = 'chrismelnyk'
import tkinter as tk
from PIL import ImageTk,Image
from tkinter import font

root = tk.Tk()
root.geometry('600x570')
root.title('Item List')

icon_img = 'images/icon_astro.jpg'
icon = ImageTk.PhotoImage(Image.open(icon_img))
root.tk.call('wm','iconphoto', root._w, icon)
#               RAW MATERIALS
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
#             REFINED MATERIALS
img_aluminium = 'images/refined/aluminum.png'
img_carbon = 'images/refined/carbon.png'
img_ceramic= 'images/refined/ceramic.png'
img_copper= 'images/refined/copper.png'
img_glass= 'images/refined/glass.png'
img_iron= 'images/refined/iron.png'
img_titanium= 'images/refined/titanium.png'
img_tungsten= 'images/refined/tungsten.png'
img_zinc= 'images/refined/zinc.png'
#            COMPOSITE RESOURCES
img_aluminium_alloy = 'images/composite/aluminum_alloy.png'
img_diamond = 'images/composite/diamond.png'
img_explosive_powder = 'images/composite/explosive_powder.png'
img_hydrazine = 'images/composite/hydrazine.png'
img_nanocarbon_alloy = 'images/composite/nanocarbon_alloy.png'
img_plastic = 'images/composite/plastic.png'
img_rubber = 'images/composite/rubber.png'
img_silicone = 'images/composite/silicone.png'
img_steel = 'images/composite/steel.png'
img_titanium_alloy = 'images/composite/titanium_alloy.png'
img_tungsten_carbide = 'images/composite/tungsten_carbide.png'
#              LOAD ALL IMAGES
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
#Refined items
aluminium_icon = ImageTk.PhotoImage(Image.open(img_aluminium))
carbon_icon = ImageTk.PhotoImage(Image.open(img_carbon))
ceramic_icon = ImageTk.PhotoImage(Image.open(img_ceramic))
copper_icon = ImageTk.PhotoImage(Image.open(img_copper))
glass_icon = ImageTk.PhotoImage(Image.open(img_glass))
iron_icon = ImageTk.PhotoImage(Image.open(img_iron))
titanium_icon = ImageTk.PhotoImage(Image.open(img_titanium))
tungsten_icon = ImageTk.PhotoImage(Image.open(img_tungsten))
zinc_icon = ImageTk.PhotoImage(Image.open(img_zinc))
#Composite items
aluminum_alloy_icon = ImageTk.PhotoImage(Image.open(img_aluminium_alloy))
diamond_icon = ImageTk.PhotoImage(Image.open(img_diamond))
explosive_powder_icon = ImageTk.PhotoImage(Image.open(img_explosive_powder))
hydrazine_icon = ImageTk.PhotoImage(Image.open(img_hydrazine))
nanocarbon_alloy_icon = ImageTk.PhotoImage(Image.open(img_nanocarbon_alloy))
plastic_icon = ImageTk.PhotoImage(Image.open(img_plastic))
rubber_icon = ImageTk.PhotoImage(Image.open(img_rubber))
silicone_icon = ImageTk.PhotoImage(Image.open(img_silicone))
steel_icon = ImageTk.PhotoImage(Image.open(img_steel))
titanium_alloy_icon = ImageTk.PhotoImage(Image.open(img_titanium_alloy))
tungsten_carbide_icon = ImageTk.PhotoImage(Image.open(img_tungsten_carbide))

tk.Label(root, text="ICON").grid(row=0, column=0,)
tk.Label(root, text="------------").grid(row=1, column=0,)
tk.Label(root, image=compound_icon, height=30, width=30).grid(row=2, column=0)
tk.Label(root, image=resin_icon, height=30, width=30).grid(row=3, column=0)
tk.Label(root, image=organic_icon, height=30, width=30).grid(row=4, column=0)
tk.Label(root, image=quartz_icon, height=30, width=30).grid(row=5, column=0)
tk.Label(root, image=wolframite_icon, height=30, width=30).grid(row=6, column=0)
tk.Label(root, image=clay_icon, height=30, width=30).grid(row=7, column=0)
tk.Label(root, image=hermatite_icon, height=30, width=30).grid(row=8, column=0)
tk.Label(root, image=malachite_icon, height=30, width=30).grid(row=9, column=0)
tk.Label(root, image=laterite_icon, height=30, width=30).grid(row=10, column=0)
tk.Label(root, image=ammonium_icon, height=30, width=30).grid(row=11, column=0)
tk.Label(root, image=graphite_icon, height=30, width=30).grid(row=12, column=0)
tk.Label(root, image=titanite_icon, height=30, width=30).grid(row=13, column=0)
tk.Label(root, image=lithium_icon, height=30, width=30).grid(row=14, column=0)
tk.Label(root, image=sphalerite_icon, height=30, width=30).grid(row=15, column=0)
tk.Label(root, image=astronium_icon, height=30, width=30).grid(row=16, column=0)

tk.Label(root, text="-").grid(row=2, column=1)
tk.Label(root, text="-").grid(row=3, column=1)
tk.Label(root, text="-").grid(row=4, column=1)
tk.Label(root, text="-").grid(row=5, column=1)
tk.Label(root, text="-").grid(row=6, column=1)
tk.Label(root, text="-").grid(row=7, column=1)
tk.Label(root, text="-").grid(row=8, column=1)
tk.Label(root, text="-").grid(row=9, column=1)
tk.Label(root, text="-").grid(row=10, column=1)
tk.Label(root, text="-").grid(row=11, column=1)
tk.Label(root, text="-").grid(row=12, column=1)
tk.Label(root, text="-").grid(row=13, column=1)
tk.Label(root, text="-").grid(row=14, column=1)
tk.Label(root, text="-").grid(row=15, column=1)
tk.Label(root, text="-").grid(row=16, column=1)

tk.Label(root, text="NAME").grid(row=0, column=2,)
tk.Label(root, text="------------").grid(row=1, column=2,)
tk.Label(root, text="Compound").grid(row=2, column=2)
tk.Label(root, text="Resin").grid(row=3, column=2)
tk.Label(root, text="Organic").grid(row=4, column=2)
tk.Label(root, text="Quartz").grid(row=5, column=2)
tk.Label(root, text="Wolframite").grid(row=6, column=2)
tk.Label(root, text="Clay").grid(row=7, column=2)
tk.Label(root, text="Hematite").grid(row=8, column=2)
tk.Label(root, text="Malachite").grid(row=9, column=2)
tk.Label(root, text="Laterite").grid(row=10, column=2)
tk.Label(root, text="Ammonium").grid(row=11, column=2)
tk.Label(root, text="Graphite").grid(row=12, column=2)
tk.Label(root, text="Titanite").grid(row=13, column=2)
tk.Label(root, text="Lithium").grid(row=14, column=2)
tk.Label(root, text="Sphalerite").grid(row=15, column=2)
tk.Label(root, text="Astronium").grid(row=16, column=2)

tk.Label(root, text="-").grid(row=2, column=3)
tk.Label(root, text="-").grid(row=3, column=3)
tk.Label(root, text="-").grid(row=4, column=3)
tk.Label(root, text="-").grid(row=5, column=3)
tk.Label(root, text="-").grid(row=6, column=3)
tk.Label(root, text="-").grid(row=7, column=3)
tk.Label(root, text="-").grid(row=8, column=3)
tk.Label(root, text="-").grid(row=9, column=3)
tk.Label(root, text="-").grid(row=10, column=3)
tk.Label(root, text="-").grid(row=11, column=3)
tk.Label(root, text="-").grid(row=12, column=3)
tk.Label(root, text="-").grid(row=13, column=3)
tk.Label(root, text="-").grid(row=14, column=3)
tk.Label(root, text="-").grid(row=15, column=3)
tk.Label(root, text="-").grid(row=16, column=3)

tk.Label(root, text="SMELTING").grid(row=0, column=4,)
tk.Label(root, text="------------").grid(row=1, column=4,)
tk.Label(root, text="n/a").grid(row=2, column=4)
tk.Label(root, text="n/a").grid(row=3, column=4)
tk.Label(root, text="Carbon").grid(row=4, column=4)
tk.Label(root, text="Glass").grid(row=5, column=4)
tk.Label(root, text="Tungsten").grid(row=6, column=4)
tk.Label(root, text="Clay").grid(row=7, column=4)
tk.Label(root, text="Hematite").grid(row=8, column=4)
tk.Label(root, text="Malachite").grid(row=9, column=4)
tk.Label(root, text="Laterite").grid(row=10, column=4)
tk.Label(root, text="Ammonium").grid(row=11, column=4)
tk.Label(root, text="Graphite").grid(row=12, column=4)
tk.Label(root, text="Titanite").grid(row=13, column=4)
tk.Label(root, text="Lithium").grid(row=14, column=4)
tk.Label(root, text="Sphalerite").grid(row=15, column=4)
tk.Label(root, text="Astronium").grid(row=16, column=4)

tk.Label(root, text="SMELT ICON").grid(row=0, column=5,)
tk.Label(root, text="------------").grid(row=1, column=5    ,)
tk.Label(root, image="").grid(row=2, column=5)
tk.Label(root, image=resin_icon, height=30, width=30).grid(row=3, column=5)
tk.Label(root, image=organic_icon, height=30, width=30).grid(row=4, column=5)
tk.Label(root, image=quartz_icon, height=30, width=30).grid(row=5, column=5)
tk.Label(root, image=wolframite_icon, height=30, width=30).grid(row=6, column=5)
tk.Label(root, image=clay_icon, height=30, width=30).grid(row=7, column=5)
tk.Label(root, image=hermatite_icon, height=30, width=30).grid(row=8, column=5)
tk.Label(root, image=malachite_icon, height=30, width=30).grid(row=9, column=5)
tk.Label(root, image=laterite_icon, height=30, width=30).grid(row=10, column=5)
tk.Label(root, image=ammonium_icon, height=30, width=30).grid(row=11, column=5)
tk.Label(root, image=graphite_icon, height=30, width=30).grid(row=12, column=5)
tk.Label(root, image=titanite_icon, height=30, width=30).grid(row=13, column=5)
tk.Label(root, image=lithium_icon, height=30, width=30).grid(row=14, column=5)
tk.Label(root, image=sphalerite_icon, height=30, width=30).grid(row=15, column=5)
tk.Label(root, image=astronium_icon, height=30, width=30).grid(row=16, column=5)






root.mainloop()