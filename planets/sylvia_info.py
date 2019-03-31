import tkinter as tk
from PIL import ImageTk,Image

root = tk.Tk()
secondLevel = tk.Frame(master=root)
root.geometry('350x650')
root.title('Astroneer Wiki')
l1 = tk.Label(text="Sylvia Planet Info", fg="black", bg="snow")

#Load images into variables
img_icon = "images/planets/planet.icon/sylvia.icon.png"
img_planet = "images/planets/planet.space/sylvia.space.png"
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
img_hydrogen = "images/gases/hydrogen.png"
img_nitrogen = "images/gases/nitrogen.png"

sylvia_planet = ImageTk.PhotoImage(Image.open(img_planet))
sylvia_icon = ImageTk.PhotoImage(Image.open(img_icon))
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
hydrogen_icon = ImageTk.PhotoImage(Image.open(img_hydrogen))
nitrogen_icon = ImageTk.PhotoImage(Image.open(img_nitrogen))

#Insert text into window
l1 = tk.Label(root, text="SYLVIA RESOURCES\n===================\nCompound\nResin\nOrganic\nClay\nGraphite\nQuartz\nLaterite\nAmmonium\nAstronium", font="Helvetica")
l1.place(x=50, y=0)

l2 = tk.Label(root, text="PRIMARY RESOURCES\n====================\nSphalerite", font="Helvetica")
l2.place(x=50, y=300)

l3 = tk.Label(root, text="SECONDARY RESOURCES\n====================\nMalachite", font="Helvetica")
l3.place(x=50, y=420)

l4 = tk.Label(root, text="GASES\n====================\nHydrogen: 75ppu\nNitrogen: 100ppu", font="Helvetica")
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

i10 = tk.Label(root, image=sphalerite_icon, height=20, width=20)
i10.place(x=55, y=350)

i11 = tk.Label(root, image=malachite_icon, height=20, width=20)
i11.place(x=55, y=470)

i12 = tk.Label(root, image=hydrogen_icon, height=20, width=20)
i12.place(x=55, y=570)

i13 = tk.Label(root, image=nitrogen_icon, height=20, width=20)
i13.place(x=55, y=595)


#Run program
root.mainloop()