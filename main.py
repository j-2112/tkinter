import tkinter as tk

root = tk.Tk()

e = tk.Entry(root, width=50)
e.pack()


def my_click():
    msg = "Hello " + e.get()
    test_label = tk.Label(root, text= msg)
    test_label.pack()

button  = tk.Button(root, text="enter your name", command=my_click)
button.pack()

root.mainloop()