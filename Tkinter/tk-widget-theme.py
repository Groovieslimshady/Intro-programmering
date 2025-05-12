import tkinter as tk
from tkinter import ttk

root = tk.Tk()
style = ttk.Style()
style.configure("TLabel", background="#02681F", foreground="White", font=("Algerian", 14))
tk.Label (root, text='classic label').pack()
ttk.Label (root, text="themed label", style="TLabel").pack()

root.geometry ("1000x600+50+50")
root.mainloop()