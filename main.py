import tkinter as tk
root = tk.Tk()

root.geometry('300x500')
root.title("Lable test title")

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