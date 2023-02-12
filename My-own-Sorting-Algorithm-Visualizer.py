# Making a window using tkinter.
import tkinter as tk
from tkinter import ttk
from tkinter import HORIZONTAL


OPTIONS = [
    "Selection Sort",
    "Bubble Sort",
    "Insertion Sort",
    "Comb Sort",
    "Cocktail Shaker Sort",
    "Heap Sort",
    "Quick Sort",
    "Bogo Sort"
]

root = tk.Tk()

# ==========STYLING==========
forStyling = ttk.Style()
forStyling.configure('mainFrame.TFrame', background = '#282A3A')
forStyling.configure('Frame2.TFrame', background = 'gray')
forStyling.configure('Frame3.TFrame', background = '#735F32')
forStyling.configure('Frame4.TFrame', background = 'black')

# ==========WIDGETS==========
# Main
mainFrame = ttk.Frame(root, width=250, height=250, style = 'mainFrame.TFrame')
mainFrame.grid()

# For Title
TitleFrame = ttk.Frame(mainFrame, width=1300, height= 100, style='Frame2.TFrame' )
TitleLabel = ttk.Label(TitleFrame, text= "        Mark's Sorting Algorithm Visualizer", background='gray', foreground='black', font=('Times', 50, 'bold italic'))
TitleLabel.grid(padx=15, pady=15, row=0, column=0, columnspan= 4, sticky='WE')
TitleFrame.grid(padx=15, pady=15, row=0, column=0, columnspan= 4, sticky='WE')

#For UI
buttonFrame = ttk.Frame(mainFrame, width= 300, height= 400, style='Frame3.TFrame' )
variable = tk.StringVar(buttonFrame)
variable.set(OPTIONS[0])  # default value
dropDown = tk.OptionMenu(buttonFrame, variable, *OPTIONS)
scale = tk.Scale(buttonFrame, from_=2, to=600 // 10, orient=HORIZONTAL, length=170, label="Size Bar")
scale.set(10)
scale_speed = tk.Scale(buttonFrame, from_=2, to=500, orient=HORIZONTAL, length=170, label="Speed")
scale_speed.set(10)
generate = tk.Button(buttonFrame, text="Generate", width=20, font="Arial", background='white', highlightcolor='red')
start = tk.Button(buttonFrame, text="Start", width=20, font="Arial", background='white', highlightcolor='red')
exit = tk.Button(buttonFrame, text="Exit", width=20, font="Arial", background='white', highlightcolor='red')

dropDown.grid(padx=15, pady=15, row=0, column=0, sticky='WE')
scale.grid(padx=15, pady=15, row=1, column=0, sticky='WE')
scale_speed.grid(padx=15, pady=15, row=2, column=0, sticky='WE')
generate.grid(padx=15, pady=15, row=3, column=0, sticky='WE')
start.grid(padx=15, pady=15, row=4, column=0, sticky='WE')
exit.grid(padx=15, pady=15, row=5, column=0, sticky='WE')


buttonFrame.grid(padx=15, pady=15, row=1, column=0, sticky='WE')

#For Simulation
simulationFrame = ttk.Frame(mainFrame, width=980, height=400, style='Frame4.TFrame' )
simulationFrame.grid(padx=15, pady=15, row=1, column=1)



# ==========GRID CONFIGURATIONS==========

root.columnconfigure(0, weight=2)
root.rowconfigure(0, weight=2)


root.mainloop()