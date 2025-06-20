from tkinter import *
 
root = Tk()
root.title("Pack vs grid")
root.iconbitmap("")
root.geometry("500x350")

btn1 = Button(root,text="Button1")
btn2 = Button(root,text="Button2")

# pack
btn1.pack(pady=(20,0))
btn2.pack(pady=0, fill=X, padx=20)

# quick frame
frm = Frame(root)
frm.pack(pady=20)

#grid stuff
btn3 = Button(frm,text='Button3')
btn4 = Button(frm,text='Button4')
btn5 = Button(frm,text='Button5')

btn6 = Button(frm,text='Button6')

btn3.grid(row=0,column=0)
btn4.grid(row=0,column=1,padx=20)
btn5.grid(row=0,column=2)
btn6.grid(row=1,column=0,pady=20,columnspan=3,sticky='ew')

root.mainloop()
