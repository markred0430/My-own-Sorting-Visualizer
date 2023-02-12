# Making a window using tkinter.
import tkinter as tk
from tkinter import ttk

root = tk.Tk()

# ==========STYLING==========
forStyling = ttk.Style()
forStyling.configure('mainFrame.TFrame', background = '#282A3A')
forStyling.configure('Frame2.TFrame', background = 'gray')
forStyling.configure('Frame3.TFrame', background = '#735F32')
forStyling.configure('Frame4.TFrame', background = 'black')

# ==========WIDGETS==========
mainFrame = ttk.Frame(root, width=250, height=250, style = 'mainFrame.TFrame')
mainFrame.grid()

TitleFrame = ttk.Frame(mainFrame, width=1300, height= 100, style='Frame2.TFrame' )
TitleLabel = ttk.Label(TitleFrame, text= "        Mark's Sorting Algorithm Visualizer", background='gray', foreground='black', font=('Times', 50, 'bold italic'))
TitleLabel.grid(padx=15, pady=15, row=0, column=0, columnspan= 4, sticky='WE')
TitleFrame.grid(padx=15, pady=15, row=0, column=0, columnspan= 4, sticky='WE')

buttonFrame = ttk.Frame(mainFrame, width= 300, height= 400, style='Frame3.TFrame' )
buttonFrame.grid(padx=15, pady=15, row=1, column=0, sticky='WE')

simulationFrame = ttk.Frame(mainFrame, width=980, height=400, style='Frame4.TFrame' )
simulationFrame.grid(padx=15, pady=15, row=1, column=1)



# ==========GRID CONFIGURATIONS==========

root.columnconfigure(0, weight=2)
root.rowconfigure(0, weight=2)
root.mainloop()