import tkinter as tk
from PIL import ImageTk,Image

root = tk.Tk()
secondLevel = tk.Frame(master=root)
root.geometry('350x700')
root.title('Vesania Planet Info')

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
img_sphalerite = "images/resources/sphalerite.png"
img_malachite = "images/resources/malachite.png"
img_wolframite = "images/resources/wolframite.png"
img_hydrogen = "images/gases/hydrogen.png"
img_nitrogen = "images/gases/nitrogen.png"
img_argon = "images/gases/argon.png"
img_methane = "images/gases/methane.png"
img_hydrogen = "images/gases/hydrogen.png"
img_lithium = "images/resources/lithium.png"
img_titanite = "images/resources/titanite.png"

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
wolframite_icon = ImageTk.PhotoImage(Image.open(img_wolframite))
hydrogen_icon = ImageTk.PhotoImage(Image.open(img_hydrogen))
nitrogen_icon = ImageTk.PhotoImage(Image.open(img_nitrogen))
argon_icon = ImageTk.PhotoImage(Image.open(img_argon))
methane_icon = ImageTk.PhotoImage(Image.open(img_methane))
hydrogen_icon = ImageTk.PhotoImage(Image.open(img_hydrogen))
lithium_icon = ImageTk.PhotoImage(Image.open(img_lithium))

#Insert text into window
l1 = tk.Label(root, text="VESANIA RESOURCES\n===================\nCompound\nResin\nOrganic\nClay\nGraphite\nQuartz\nLaterite\nAmmonium\nAstronium", font="Helvetica")
l1.place(x=50, y=0)

l2 = tk.Label(root, text="PRIMARY RESOURCES\n====================\nLithium", font="Helvetica")
l2.place(x=50, y=300)

l3 = tk.Label(root, text="SECONDARY RESOURCES\n====================\nTitanite", font="Helvetica")
l3.place(x=50, y=420)

l4 = tk.Label(root, text="GASES\n====================\nHydrogen: 100 ppu\nArgon: 50ppu\nNitrogen:75 ppu", font="Helvetica")
l4.place(x=50, y=520)

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

i10 = tk.Label(root, image=lithium_icon, height=20, width=20)
i10.place(x=55, y=350)

i11 = tk.Label(root, image=titanite_icon, height=20, width=20)
i11.place(x=55, y=470)

i12 = tk.Label(root, image=hydrogen_icon, height=20, width=20)
i12.place(x=55, y=565)

i13 = tk.Label(root, image=argon_icon, height=20, width=20)
i13.place(x=55, y=590)

i14 = tk.Label(root, image=nitrogen_icon, height=20, width=20)
i14.place(x=55, y=615)

#Run program
root.mainloop()