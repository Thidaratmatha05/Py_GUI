from tkinter import * ;
root = Tk()



frame = Frame(root,bd=3, height=300, width=500, relief=GROOVE, cursor="hand1" , highlightthickness=20)
frame.pack()

Button(frame,text="01").grid(row=1,column=0)
Button(frame,text="02").grid(row=2,column=0)
Button(frame,text="02").grid(row=3,column=0)
Button(frame,text="02").grid(row=4,column=0)
Button(frame,text="02").grid(row=5,column=0)
Button(frame,text="02").grid(row=6,column=0)
Button(frame,text="02").grid(row=7,column=0)
Button(frame,text="02").grid(row=8,column=0)
Button(frame,text="02").grid(row=9,column=0)
Button(frame,text="02").grid(row=10,column=0)
Button(frame,text="02").grid(row=11,column=0)
Button(frame,text="02").grid(row=12,column=0)
Button(frame,text="13").grid(row=13,column=0)
Button(frame,text="13,2").grid(row=13,column=2)

root.mainloop()