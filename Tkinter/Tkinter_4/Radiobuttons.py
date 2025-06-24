# Tkinter tute 4
# azltech june 2025
# from tkinter.com

from tkinter import *
 
root = Tk()
root.title("Radiobuttons")
root.iconbitmap("")
root.geometry("600x400")

# clicked function
def clicked():
    lbl.config(text=f'You picked {radvar.get()}!')
    
# create button function
def selector():
    radvar.set('Your nose!')
    clicked()

def make():
    lbl.config(text=f'You picked {radvar.get()}!')

# create a Tkinter Var (IntVar, StringVar)
radvar = StringVar()

#create radio buttons
rbn1 = Radiobutton(root,text='Pepperoni',variable=radvar,value='Pepperoni')
rbn1.pack(pady=(40,10))
rbn2 = Radiobutton(root,text='Cheese',variable=radvar,value='Cheese')
rbn2.pack(pady=(40,10))
rbn3 = Radiobutton(root,text='Your nose!',variable=radvar,value='Your nose!')
rbn3.pack(pady=(40,10))

# set default radiobutton
radvar.set('Pepperoni')

# label to display choice
lbl = Label(root,text='',font=('Menlo',18))
lbl.pack(pady=10)

# create a buttons
btn = Button(root,text='Select Mushroom',command=selector)
btn.pack(pady=10)

btn2 = Button(root,text='Make a Selection',command=make)
btn2.pack(pady=10)

root.mainloop()
