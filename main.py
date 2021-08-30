# "TODO: add doc strings as well as formatting. Make sure pull requests are working"
"""Here is a general doc string. I need to make sure my python file is updated with some
of the info that tkinter needs. I want better documentation to help me better understand
what is going on"""

import tkinter as tk

root = tk.Tk()

test = tk.Entry(root, width=50)
test.pack()

e2 = tk.Entry(root, width=75)
e2.pack()

bs_label = tk.Label(root, text="this is the bs label")
bs_label.pack()

def my_click():
    msg = "Hello " + test.get()
    test_label = tk.Label(root, text= msg)
    test_label.pack()

button  = tk.Button(root, text="enter your name", command=my_click)
button.pack()

root.mainloop()