from tkinter import * ;

root =Tk()
root.title("My App K GUI")

Label(bg="black").pack()
Label(text="...โปรแกรม...",font=60,fg="white",bg="black").pack()
Label(text="...โปรแกรม...",font=60,fg="white",bg="black").pack()
Label(bg="black").pack()

frame = Frame(root,bd=3, height=10, width=10, relief=RIDGE, cursor="hand1" , highlightthickness=0)
frame.pack()

#row=0
Label(frame,text=" ลำดับที่ ",bg = "white",font=55).grid(row=0,column=0)
Label(frame,text="").grid(row=0,column=1)
Label(frame,text=" ข้อมูล01 ",bg = "white",font=55).grid(row=0,column=2)
Label(frame,text="").grid(row=0,column=3)
Label(frame,text=" ข้อมูล02 ",bg = "white",font=55).grid(row=0,column=4)
Label(frame,text="").grid(row=0,column=5)
Label(frame,text=" ข้อมูล03 ",bg = "white",font=55).grid(row=0,column=6)
Label(frame,text="").grid(row=0,column=7)
Label(frame,text=" ข้อมูล04 ",bg = "white",font=55).grid(row=0,column=8)

#row=1
Label(frame,text="01",font=50).grid(row=1,column=0)
Label(frame,text="").grid(row=1,column=1)
Label(frame,text="01",font=50).grid(row=1,column=2)
Label(frame,text="").grid(row=1,column=3)
Label(frame,text="02",font=50).grid(row=1,column=4)
Label(frame,text="").grid(row=1,column=5)
Label(frame,text="03",font=50).grid(row=1,column=6)
Label(frame,text="").grid(row=1,column=7)
Label(frame,text="04",font=50).grid(row=1,column=8)

#row=2
Label(frame,text="02",font=50).grid(row=2,column=0)
Label(frame,text="").grid(row=2,column=1)
Label(frame,text="01",font=50).grid(row=2,column=2)
Label(frame,text="").grid(row=2,column=3)
Label(frame,text="02",font=50).grid(row=2,column=4)
Label(frame,text="").grid(row=2,column=5)
Label(frame,text="03",font=50).grid(row=2,column=6)
Label(frame,text="").grid(row=2,column=7)
Label(frame,text="04",font=50).grid(row=2,column=8)

#row=3
Label(frame,text="03",font=50).grid(row=3,column=0)
Label(frame,text="").grid(row=3,column=1)
Label(frame,text="01",font=50).grid(row=3,column=2)
Label(frame,text="").grid(row=3,column=3)
Label(frame,text="02",font=50).grid(row=3,column=4)
Label(frame,text="").grid(row=3,column=5)
Label(frame,text="03",font=50).grid(row=3,column=6)
Label(frame,text="").grid(row=3,column=7)
Label(frame,text="04",font=50).grid(row=3,column=8)

#row=4
Label(frame,text="04",font=50).grid(row=4,column=0)
Label(frame,text="").grid(row=4,column=1)
Label(frame,text="01",font=50).grid(row=4,column=2)
Label(frame,text="").grid(row=4,column=3)
Label(frame,text="02",font=50).grid(row=4,column=4)
Label(frame,text="").grid(row=4,column=5)
Label(frame,text="03",font=50).grid(row=4,column=6)
Label(frame,text="").grid(row=4,column=7)
Label(frame,text="04",font=50).grid(row=4,column=8)

#row=5
Label(frame,text="05",font=50).grid(row=5,column=0)
Label(frame,text="").grid(row=5,column=1)
Label(frame,text="01",font=50).grid(row=5,column=2)
Label(frame,text="").grid(row=5,column=3)
Label(frame,text="02",font=50).grid(row=5,column=4)
Label(frame,text="").grid(row=5,column=5)
Label(frame,text="03",font=50).grid(row=5,column=6)
Label(frame,text="").grid(row=5,column=7)
Label(frame,text="04",font=50).grid(row=5,column=8)

#row=6
Label(frame,text="06",font=50).grid(row=6,column=0)
Label(frame,text="").grid(row=6,column=1)
Label(frame,text="01",font=50).grid(row=6,column=2)
Label(frame,text="").grid(row=6,column=3)
Label(frame,text="02",font=50).grid(row=6,column=4)
Label(frame,text="").grid(row=6,column=5)
Label(frame,text="03",font=50).grid(row=6,column=6)
Label(frame,text="").grid(row=6,column=7)
Label(frame,text="04",font=50).grid(row=6,column=8)

#row=7
Label(frame,text="07",font=50).grid(row=7,column=0)
Label(frame,text="",font=50).grid(row=7,column=1)
Label(frame,text="01",font=50).grid(row=7,column=2)
Label(frame,text="",font=50).grid(row=7,column=3)
Label(frame,text="02",font=50).grid(row=7,column=4)
Label(frame,text="",font=50).grid(row=7,column=5)
Label(frame,text="03",font=50).grid(row=7,column=6)
Label(frame,text="").grid(row=7,column=7)
Label(frame,text="04",font=50).grid(row=7,column=8)

#row=8
Label(frame,text="08",font=50).grid(row=8,column=0)
Label(frame,text="").grid(row=8,column=1)
Label(frame,text="01",font=50).grid(row=8,column=2)
Label(frame,text="").grid(row=8,column=3)
Label(frame,text="02",font=50).grid(row=8,column=4)
Label(frame,text="").grid(row=8,column=5)
Label(frame,text="03",font=50).grid(row=8,column=6)
Label(frame,text="").grid(row=8,column=7)
Label(frame,text="04",font=50).grid(row=8,column=8)

#row=9
Label(frame,text="09",font=50).grid(row=9,column=0)
Label(frame,text="").grid(row=9,column=1)
Label(frame,text="01",font=50).grid(row=9,column=2)
Label(frame,text="").grid(row=9,column=3)
Label(frame,text="02",font=50).grid(row=9,column=4)
Label(frame,text="",font=50).grid(row=9,column=5)
Label(frame,text="03",font=50).grid(row=9,column=6)
Label(frame,text="").grid(row=9,column=7)
Label(frame,text="04",font=50).grid(row=9,column=8)

#row=10
Label(frame,text="10",font=50).grid(row=10,column=0)
Label(frame,text="").grid(row=10,column=1)
Label(frame,text="01",font=50).grid(row=10,column=2)
Label(frame,text="").grid(row=10,column=3)
Label(frame,text="02",font=50).grid(row=10,column=4)
Label(frame,text="").grid(row=10,column=5)
Label(frame,text="03",font=50).grid(row=10,column=6)
Label(frame,text="").grid(row=10,column=7)
Label(frame,text="04",font=50).grid(row=10,column=8)


frame2 = Frame(root,bd=3, height=10, width=10, relief=RIDGE, cursor="hand1" , highlightthickness=1)
frame2.pack()


#row=0
Label(frame2,text="ลำดับที่ K ",bg = "white",font=50).grid(row=0,column=0)
Label(frame2,text="ข้อมูลที่1",bg = "white",font=50).grid(row=0,column=1)

Label(frame2,text="").grid(row=0,column=2)
Label(frame2,text="ข้อมูลที่2",bg = "white",font=50).grid(row=0,column=3)

Label(frame2,text="").grid(row=0,column=4)
Label(frame2,text="ข้อมูลที่3",bg = "white",font=50).grid(row=0,column=5)

Label(frame2,text="").grid(row=0,column=6)
Label(frame2,text=" ทำนายผล ",bg = "white",font=50).grid(row=0,column=7)


#row=1
txt = StringVar()
mytxt = Entry(frame2,textvariable=txt,font=50)
mytxt.grid(row=1,column=0)
#txt01 = IntVar()
txt01 = StringVar()
mytxt01 = Entry(frame2,textvariable=txt01,font=50)
mytxt01.grid(row=1,column=1)

Label(frame2,text="").grid(row=1,column=2)
txt02 = StringVar()
mytxt02 = Entry(frame2,textvariable=txt02,font=50)
mytxt02.grid(row=1,column=3)

Label(frame2,text="").grid(row=1,column=4)
txt03 = StringVar()
mytxt03 = Entry(frame2,textvariable=txt03,font=50)
mytxt03.grid(row=1,column=5)

Label(frame2,text="").grid(row=1,column=6)

#row=3
#Label(frame2,text="ผลทำนาย").grid(row=2,column=0)

Label(frame2,text="").grid(row=2,column=2)
Label(frame2,text="").grid(row=2,column=4)
Label(frame2,text="").grid(row=2,column=6)

#row=3 , showtxt
def showText():
    Message = txt.get()
    print(Message)
    la_txex = Label(frame2,text=Message,font=50).grid(row=2,column=0)

    Message01 = txt01.get()
    print(Message01)
    la_txex01 = Label(frame2,text=Message01,font=50).grid(row=2,column=1)

    Message02 = txt02.get()
    print(Message02)
    la_txex02 = Label(frame2,text=Message02,font=50).grid(row=2,column=3)

    Message03 = txt03.get()
    print(Message03)
    la_txex03 = Label(frame2,text=Message03,font=50).grid(row=2,column=5)


    mytxt.delete(0,END)
    mytxt01.delete(0,END)
    mytxt02.delete(0,END)
    mytxt03.delete(0,END)


def deleteText():
    mytxt.delete(0,END)
    mytxt01.delete(0,END)
    mytxt02.delete(0,END)
    mytxt03.delete(0,END)



#row=4
buttonShow = Button(frame2,text='ทำนาย', command=showText, bg="red",font=50).grid(row=3,column=5)
#buttondelete = Button(frame2,text='deleteText', command=deleteText).grid(row=3,column=7)


#กำหนดขนาดหน้าต่าง
root.configure(bg='black')
root.geometry("900x600")
root.mainloop()