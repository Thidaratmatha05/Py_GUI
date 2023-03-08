from tkinter import * ;

root =Tk()
root.title("GUI")

#ใส่ข้อความ
#Label(text="โปรแกรม...",font=40,fg="red",bg="green").pack()
#  myLabal = Label(text=".W.",font=20).pack(anchor=W)
#  myLabal = Label(text=".E.",font=20).pack(anchor=E)
#  myLabal = Label(text="โปรแกรม...",font=40).pack()
#  myLabal = Label(text="...",font=40).place(x=250,y=100)

myLabal = Label(text="...0...",font=40).grid(row=0,column=0)

#กล่องข้อความ
txt = StringVar()
mytxt = Entry(textvariable=txt).grid(row=0,column=1)

def showtxt():
    Message = txt.get()
    print(Message)
    myLabaltxt = Label(text=Message,font=40).grid(row=10,column=0)



button = Button(text='click me!', command=showtxt).grid(row=0,column=3)

myLabal = Label(text="Message",font=40).grid(row=5,column=0,)




Label(text="r=0,C=0",font=40).grid(row=0,column=0,sticky=N)
Label(text="...r=1,C=0...",font=40).grid(row=1,column=0)

#txet data row=2
Button(text='!').grid(row=2,column=0)
Button(text='ลำดับ').grid(row=2,column=1)
Button(text='ข้อมูล1').grid(row=2,column=2)
Button(text='ข้อมูล2').grid(row=2,column=3)
Button(text='ข้อมูล3').grid(row=2,column=4)
Button(text='ข้อมูล4').grid(row=2,column=5)


#btn  btn2 = Button(rootตรงนี้คือหน้าจอที่อยู่,text="ยกเลิก",font=40,fg="white",bg="red").pack()
#  btn1 = Button(text="ทำนาย",font=40,fg="white",bg="green").pack()
#  btn2 = Button(root,text="ยกเลิก",font=40,fg="white",bg="red").pack()
#  button = Button(text='click me!', command=print_something).pack()

#  e1 = Entry().pack()


#กำหนดขนาดหน้าต่าง
root.geometry("960x540")
root.mainloop()