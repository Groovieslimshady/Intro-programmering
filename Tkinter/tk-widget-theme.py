import tkinter as tk
from tkinter import ttk

root = tk.Tk()

tk.Label (root, text='classic label').pack()
ttk.Label (root, text="themed label").pack()

root.geometry ("1000x600+50+50")
root.mainloop()