# Making a window using tkinter.
import tkinter as tk
from tkinter import ttk

root = tk.Tk()

#Styling Frame
pampaganda = ttk.Style()
pampaganda.configure('mainFrame.TFrame', background = '#282A3A')

#create a main window frame
mainFrame = ttk.Frame(root, width = 1250, height = 1250, style='mainFrame.TFrame')
canvas = tk.Canvas(root, bg="black", height=1250, width=1250)
root.title("Sorting")
mainFrame.grid()


root.resizable(width = False, height = False)
root.mainloop()