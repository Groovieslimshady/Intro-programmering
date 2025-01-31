import tkinter as tk
from tkinter import messagebox
root = tk.Tk()
root.title("BlackJack")
root.geometry ("1000x600+120+40")

messagebox.askokcancel ("ja eller nej", "vill du fortsätta?")

root.iconbitmap('C:/Pythonkaka/blackjack.ico')
root.mainloop()