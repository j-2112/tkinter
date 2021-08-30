import tkinter as tk
root = tk.Tk()

root.geometry('300x500+75+200')
root.title("CAT COUNTER")
photo = tk.PhotoImage(file='cat.png')
root.iconphoto(False, photo)


root.mainloop()