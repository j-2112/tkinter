from tkinter import *
root = Tk()

root.geometry('300x500')
root.title("Lable test title")

# show a label below
bs_label = Label(root, 
    text="This is a label", 
    font=("Helvetica", 15))
bs_label.pack()


root.mainloop()