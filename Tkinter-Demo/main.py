from tkinter import *


def button_clicked():
    print("I got clicked")
    mylabel.config(text="BUtton got clicked.")

window = Tk()
window.title("My First GUI program")
window.minsize(width=500, height=300)

mylabel = Label(text="I am a Label", font=("Aerial",24))
mylabel.config(text = "new text")
mylabel.grid(column=0, row=0)


button = Button(text="Click me", command=button_clicked)
button.grid(column=1,row=1)

new_button = Button(text="New Button")
new_button.grid(column=2, row = 0)

input = Entry(width=10)
print(input.get())
input.grid(column=2, row=2)
window.mainloop()