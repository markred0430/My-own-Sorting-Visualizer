# Making a window using tkinter.
import tkinter as tk
import random
from tkinter import ttk
from tkinter import HORIZONTAL

# ===========================LIST OF SORTING ALGORITHMS=====================
OPTIONS = [
    "Selection Sort",
    "Bubble Sort",
    "Insertion Sort",
    "Comb Sort",
    "Cocktail Shaker Sort",
    "Bogo Sort"
]

# ===========================COLOR FILL FOR THE BARS=====================
def colorBar(col, color):
    canvas.itemconfig(col, fill=color)

# ===========================Function that will swap two bars in simulation that will be animated=====================
def swap(pos_0, pos_1):
    bar11, _, bar12, _ = canvas.coords(pos_0)
    bar21, x, bar22, _ = canvas.coords(pos_1)
    canvas.itemconfig(pos_0, fill='red')
    canvas.itemconfig(pos_1, fill='white')
    canvas.move(pos_0, bar21 - bar11, 0)
    canvas.move(pos_1, bar12 - bar22, 0)




# ===========================GUI TKINTER=====================
root = tk.Tk()
root.geometry("1100x700")
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
TitleLabel = ttk.Label(TitleFrame, text= "Mark's Sorting Algorithm Visualizer", background='gray', foreground='black', font=('Times', 50, 'bold italic'))
TitleLabel.grid(padx=15, pady=15, row=0, column=0, columnspan= 4, sticky='WE')
TitleFrame.grid(padx=15, pady=15, row=0, column=0, columnspan= 4, sticky='WE')

#For UI
buttonFrame = ttk.Frame(mainFrame, width= 600, height= 600, style='Frame3.TFrame' )
variable = tk.StringVar(buttonFrame)
variable.set(OPTIONS[0])  # default value
dropDown = tk.OptionMenu(buttonFrame, variable, *OPTIONS)
dropDown.configure(background='#C69749', foreground='#282A3A', activebackground='#282A3A', activeforeground='#C69749')
scale = tk.Scale(buttonFrame, from_=2, to=600 // 10, orient=HORIZONTAL, length=170, label="Size Bar",  font=('Times', 10), background='#C69749', foreground='#282A3A')
scale.set(10)
scale_speed = tk.Scale(buttonFrame, from_=2, to=500, orient=HORIZONTAL, length=170, label="Speed",  font=('Times', 10), background='#C69749', foreground='#282A3A')
scale_speed.set(10)
Generate = tk.Button(buttonFrame, text="Generate", width=20, font=('Times', 20), background='#C69749', highlightcolor='red', foreground='#282A3A', relief='raised', activebackground='black', activeforeground='#C69749')
Start = tk.Button(buttonFrame, text="Start", width=20, font=('Times', 20), background='#C69749', highlightcolor='red', foreground='#282A3A', relief='raised', activebackground='black', activeforeground='#C69749')
exit = tk.Button(buttonFrame, text="Exit", width=20, font=('Times', 20), background='#C69749', highlightcolor='red',  command=root.quit, foreground='#282A3A', relief='raised', activebackground='black', activeforeground='#C69749')

dropDown.grid(padx=15, pady=15, row=0, column=0, sticky='WE')
scale.grid(padx=15, pady=15, row=1, column=0, sticky='WE')
scale_speed.grid(padx=15, pady=15, row=2, column=0, sticky='WE')
Generate.grid(padx=15, pady=15, row=3, column=0, sticky='WE')
Start.grid(padx=15, pady=15, row=4, column=0, sticky='WE')
exit.grid(padx=15, pady=15, row=5, column=0, sticky='WE')


buttonFrame.grid(padx=15, pady=15, row=1, column=0, sticky='WE')

#For Simulation
simulationFrame = ttk.Frame(mainFrame, width=500, height=500, style='Frame4.TFrame' )
canvas = tk.Canvas(simulationFrame, bg="black", height=500, width=500, highlightcolor='black')
canvas.grid(padx=15, pady=15, row=0, column=0)
simulationFrame.grid(padx=15, pady=15, row=1, column=1)



# ==========GRID CONFIGURATIONS==========

root.columnconfigure(0, weight=2)
root.rowconfigure(0, weight=2)


root.resizable(width=False, height=False)
root.mainloop()