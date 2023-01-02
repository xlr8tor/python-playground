from tkinter import *
from tkinter import ttk

window = Tk()
window.geometry("800x500")
window.title("Calculator")


label = Label(window, text="Hello world")
label.pack()

buttonFrame = Frame(window)
buttonFrame.columnconfigure(0, weight=1)
buttonFrame.columnconfigure(1, weight=1)
buttonFrame.columnconfigure(2, weight=1)

btn1 = Button(buttonFrame, font=('Arial', 18), text='1')
btn1.grid(column=0, row=0, sticky=W+E)

btn2 = Button(buttonFrame, font=('Arial', 18), text='2')
btn2.grid(column=1, row=0, sticky=W+E)

btn3 = Button(buttonFrame, font=('Arial', 18), text='3')
btn3.grid(column=2, row=0, sticky=W+E)

btn4 = Button(buttonFrame, font=('Arial', 18), text='4')
btn4.grid(column=0, row=1, sticky=W+E)

btn5 = Button(buttonFrame, font=('Arial', 18), text='5')
btn5.grid(column=1, row=1, sticky=W+E)

btn6 = Button(buttonFrame, font=('Arial', 18), text='6')
btn6.grid(column=2, row=1, sticky=W+E)
# frm = ttk.Frame(window, padding=10)
# frm.grid()

# ttk.Label(frm, text="Hello world").grid(column=0, row=0)
# ttk.Button(frm, text="Quit", command=window.destroy).grid(column=1, row=0)
buttonFrame.pack(fill='x')
window.mainloop()
