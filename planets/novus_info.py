import tkinter as tk
from PIL import ImageTk,Image

root = tk.Tk()
secondLevel = tk.Frame(master=root)
root.geometry('350x600')
root.title('Novus Planet Info')

icon_img = 'images/icon_astro.jpg'
icon = ImageTk.PhotoImage(Image.open(icon_img))
root.tk.call('wm','iconphoto', root._w, icon)

#Load images into variables
img_comound = "images/resources/compound.png"
img_resin = "images/resources/resin.png"
img_organic = "images/resources/organic.png"
img_clay = "images/resources/clay.png"
img_graphite = "images/resources/graphite.png"
img_quartz = "images/resources/quartz.png"
img_laterite = "images/resources/laterite.png"
img_ammonium = "images/resources/ammonium.png"
img_astronium = "images/resources/astronium.png"
img_lithium = "images/resources/lithium.png"
img_titanite = "images/resources/titanite.png"
img_hermatite = "images/resources/hematite.png"
img_argon = "images/gases/argon.png"
img_methane = "images/gases/methane.png"
img_hydrogen = "images/gases/hydrogen.png"

compound_icon = ImageTk.PhotoImage(Image.open(img_comound))
resin_icon = ImageTk.PhotoImage(Image.open(img_resin))
organic_icon = ImageTk.PhotoImage(Image.open(img_organic))
clay_icon = ImageTk.PhotoImage(Image.open(img_clay))
graphite_icon = ImageTk.PhotoImage(Image.open(img_graphite))
quartz_icon = ImageTk.PhotoImage(Image.open(img_quartz))
laterite_icon = ImageTk.PhotoImage(Image.open(img_laterite))
ammonium_icon = ImageTk.PhotoImage(Image.open(img_ammonium))
astronium_icon = ImageTk.PhotoImage(Image.open(img_astronium))
lithium_icon = ImageTk.PhotoImage(Image.open(img_lithium))
titanite_icon = ImageTk.PhotoImage(Image.open(img_titanite))
hermatite_icon = ImageTk.PhotoImage(Image.open(img_hermatite))
argon_icon = ImageTk.PhotoImage(Image.open(img_argon))
methane_icon = ImageTk.PhotoImage(Image.open(img_methane))
hydrogen_icon = ImageTk.PhotoImage(Image.open(img_hydrogen))

#Insert text into window
l1 = tk.Label(root, text="NOVUS RESOURCES\n===================\nCompound\nResin\nOrganic\nClay\nGraphite\nQuartz\nLaterite\nAmmonium\nAstronium", font="Helvetica")
l1.config(font=("Helvetica", 15))
l1.place(x=50, y=0)

l2 = tk.Label(root, text="PRIMARY RESOURCES\n====================\nHematite", font="Helvetica")
l2.config(font=("Helvetica", 15))
l2.place(x=50, y=300)

l3 = tk.Label(root, text="SECONDARY RESOURCES\n====================\nLithium", font="Helvetica")
l3.config(font=("Helvetica", 15))
l3.place(x=50, y=400)

l4 = tk.Label(root, text="GASES\n====================\nHydrogen: 25ppu\nMethane: 75 ppu", font="Helvetica")
l4.config(font=("Helvetica", 15))
l4.place(x=50, y=500)

#Insert icons into window
i1 = tk.Label(root, image=compound_icon, height=20, width=20)
i1.place(x=55, y=45)

i2 = tk.Label(root, image=resin_icon, height=20, width=20)
i2.place(x=55, y=70)

i3 = tk.Label(root, image=organic_icon, height=20, width=20)
i3.place(x=55, y=95)

i4 = tk.Label(root, image=clay_icon, height=20, width=20)
i4.place(x=55, y=115)

i5 = tk.Label(root, image=graphite_icon, height=20, width=20)
i5.place(x=55, y=140)

i6 = tk.Label(root, image=quartz_icon, height=20, width=20)
i6.place(x=55, y=165)

i7 = tk.Label(root, image=laterite_icon, height=20, width=20)
i7.place(x=55, y=190)

i8 = tk.Label(root, image=ammonium_icon, height=20, width=20)
i8.place(x=55, y=215)

i9 = tk.Label(root, image=astronium_icon, height=20, width=20)
i9.place(x=55, y=235)

i10 = tk.Label(root, image=hermatite_icon, height=20, width=20)
i10.place(x=55, y=350)

i11 = tk.Label(root, image=lithium_icon, height=20, width=20)
i11.place(x=55, y=450)

i11 = tk.Label(root, image=hydrogen_icon, height=20, width=20)
i11.place(x=55, y=550)

i12 = tk.Label(root, image=methane_icon, height=20, width=20)
i12.place(x=55, y=575)


#Run program
root.mainloop()