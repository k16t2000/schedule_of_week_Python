from tkinter import *
import time
def esm():
    print("Single Click, Button-l")
    display_area.config(text="Esmaspäev\n\n8.30 - 10.00\tMatemaatika\n\n10.15 - 12.30\tAjalugu",fg="black",bg="white")
def teis():
    print("Single Click, Button-l")
    display_area['text'] = "Teisipäev\n\n8.30 - 10.00\tEesti keel\n10.15 - 12.00\tKehaline kasvatus"
def kolm():
    print("Single Click, Button-l")
    display_area['text'] = "Kolmapäev\n\n8.30 - 10.00\tMatemaatika\n10.15 - 12.00\tJoonistamine"
def nel():
    print("Single Click, Button-l")
    display_area['text'] = "Neljapäev\n\n8.30 - 10.00\tEesti keel\n10.15 - 12.00\tMeisterdamine"
def red():
    print("Single Click, Button-l")
    display_area['text'] = "Reede\n\n8.30 - 10.00\tMatemaatika\n10.15 - 12.00\tMuusika"
def lau():
    print("Single Click, Button-l")
    display_area['text'] = "Laupäev\n\nVaba päev"
def puh():
    print("Single Click, Button-l")
    display_area['text'] = "Pühapäev\n\nVaba päev"
def tick():#TIME
    time_label['text'] = time.strftime('%H:%M:%S')
    time_label.after(200, tick)

root=Tk()
frame = Frame(root, bg="black")
l1 =Label(root,
            text="Tunniplaan",
            padx="120",
            pady="10",
            # width=220,height=140,
            relief=GROOVE,
            justify=RIGHT,
            compound = RIGHT,
            font="Gupter 14")
#TIME
time_label = Label(font='Gupter 16')
time_label.pack(side=TOP,anchor=NE)
tick()#time_label.after_idle(tick) #это также работает

#button widget
button1=Button(frame,text="Esmaspäev",padx=30,pady=3,width=5,height=1,activebackground="#696969",activeforeground="#000000",font="Gupter 12",borderwidth=7,relief=RAISED,command=esm).pack(side=TOP,anchor=NW)
but2=Button(frame,text="Teisipäev",padx=30,pady=3,width=5,height=1,activebackground="#696969",activeforeground="#000000",font="Gupter 12",borderwidth=7,relief=RAISED, command=teis).pack(side=TOP,anchor=NW)
but3=Button(frame,text="Kolmapäev",padx=30,pady=3,width=5,height=1,activebackground="#696969",activeforeground="#000000",font="Gupter 12",borderwidth=7,relief=RAISED, command=kolm).pack(side=TOP,anchor=NW)
but4=Button(frame,text="Neljapäev",padx=30,pady=3,width=5,height=1,activebackground="#696969",activeforeground="#000000",font="Gupter 12",borderwidth=7,relief=RAISED, command=nel).pack(side=TOP,anchor=NW)
but5=Button(frame,text="Reede",padx=30,pady=3,width=5,height=1,activebackground="#696969",activeforeground="#000000",font="Gupter 12",borderwidth=7,relief=RAISED, command=red).pack(side=TOP,anchor=NW)
but6=Button(frame,text="Laupäev",padx=30,pady=3,width=5,height=1,activebackground="#696969",activeforeground="#000000",font="Gupter 12",borderwidth=7,relief=RAISED, command=lau).pack(side=TOP,anchor=NW)
but7=Button(frame,text="Pühapäev",padx=30,pady=3,width=5,height=1,activebackground="#696969",activeforeground="#000000",font="Gupter 12",borderwidth=7,relief=RAISED, command=puh).pack(side=TOP,anchor=NW)
#adding display area-using the label widget
display_area=Label(frame,text="",width=40,height=10)


frame.pack(side=BOTTOM,fill="both", expand="yes")
l1.pack(side=TOP,anchor=W)
display_area.pack(side=TOP,anchor=CENTER)
root.mainloop()
