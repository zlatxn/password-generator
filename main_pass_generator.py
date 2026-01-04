import tkinter as tk
import tkinter.font as tkFont
import string
import random


root = tk.Tk()
root.title("Password Generator 1337")
root.geometry("400x200")
root.option_add("*Font", tkFont.Font(family="Arial", size=50))


input_var = tk.IntVar(value=8)
tk.Label(root, text="Länge Wählen:").pack(padx=10, pady=6)
tk.Spinbox(root, from_=4, to=64, textvariable=input_var).pack()

out = tk.Entry(root, width=40)
out.pack(padx=16, pady=10)


def gen():
    n = int(input_var.get())
    pwd = ""
    letter_options = string.ascii_letters + string.digits

    for i in range(n):
        pwd += random.choice(letter_options)

    out.delete(0, "end")
    out.insert(0, pwd)


def copy_to_clip():
    root.clipboard_clear()
    root.clipboard_append(out.get())


tk.Button(root, text="Generate", command=gen).pack()
tk.Button(root, text="copy to clipboard", command=copy_to_clip).pack()

root.mainloop()
