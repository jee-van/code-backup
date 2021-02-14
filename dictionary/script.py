from tkinter import *

window = Tk(className='Converter')

def convert():
    KG = int(kg.get())
    grams = KG * 1000
    pounds = KG * 2.20462
    ounces = KG * 35.274
    result = f'{grams} grams\n{pounds} pounds\n{ounces} ounces'
    t1.insert(END, result)


kg = StringVar()

b1 = Button(window, text='convert', command=convert)
b1.grid(row=1, column=2)

e1 = Entry(window, textvariable=kg)
e1.grid(row=1, column=1)

t1 = Text(window,height=4, width=27)
t1.grid(row=3, columnspan=3)

temp3 = Label(window)
temp3.grid(row=4, columnspan=3)

temp2 = Label(window)
temp2.grid(row=2, columnspan=3)

temp1 = Label(window)
temp1.grid(row=0, columnspan=3)

window.mainloop()
