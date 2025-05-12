import tkinter as tk
import webbrowser




def button_clicked(): 
    webbrowser.open("https://www.youtube.com/watch?v=dQw4w9WgXcQ") 

root = tk.Tk()

root.geometry ("1000x500+50+50")
button = tk.Button(root, text="click me", command= button_clicked)

button.pack(padx=40, pady=40)

root.mainloop()