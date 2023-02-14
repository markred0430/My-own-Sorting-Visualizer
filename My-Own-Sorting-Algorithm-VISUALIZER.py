import tkinter as tk
import random
from tkinter import ttk
from tkinter import HORIZONTAL
import numpy as np
import simpleaudio as sa

# ===========================LIST OF SORTING ALGORITHMS=====================
OPTIONS = [
    "Selection Sort",
    "Bubble Sort",
    "Insertion Sort",
    "Comb Sort",
    "Cocktail Shaker Sort",
    "Bogo Sort"
]
# ===========================SORTING ALGORITHMS=====================
# -------------------------------------------SELECTION SORT------------------------------------------
def selection_Sort():
    global barList
    global lengthList

    for i in range(len(lengthList)):
        min = i
        for j in range(i + 1, len(lengthList)):
            if (lengthList[j] < lengthList[min]):
                min = j
        lengthList[min], lengthList[i] = lengthList[i], lengthList[min]
        barList[min], barList[i] = barList[i], barList[min]
        swap(barList[min], barList[i])
        yield

# -------------------------------------------BUBBLE SORT------------------------------------------------
def bubble_Sort():
    global barList
    global lengthList

    for i in range(len(lengthList) - 1):
        for j in range(len(lengthList) - i - 1):
            if (lengthList[j] > lengthList[j + 1]):
                lengthList[j], lengthList[j + 1] = lengthList[j + 1], lengthList[j]
                barList[j], barList[j + 1] = barList[j + 1], barList[j]
                swap(barList[j + 1], barList[j])
                colorBar(barList[-i], 'white')
                yield
            else:
                colorBar(barList[j], 'white')

# -------------------------------------------INSERTION SORT------------------------------------------------

def insertion_Sort():
    global barList
    global lengthList

    for i in range(len(lengthList)):
        cursor = lengthList[i]
        cursorBar = barList[i]
        pos = i

        while pos > 0 and lengthList[pos - 1] > cursor:
            lengthList[pos] = lengthList[pos - 1]
            barList[pos], barList[pos - 1] = barList[pos - 1], barList[pos]
            swap(barList[pos], barList[pos - 1])
            yield
            pos -= 1

        lengthList[pos] = cursor
        barList[pos] = cursorBar
        swap(barList[pos], cursorBar)

# -------------------------------------------COMB SORT------------------------------------------------
def comb_Sort():
    global barList
    global lengthList

    n = len(lengthList)
    gap = n
    shrink = 1.3
    sorted = False
    while not sorted:
        gap = int(gap / shrink)
        if gap > 1:
            sorted = False
        else:
            gap = 1
            sorted = True

        i = 0
        while i + gap < n:
            if lengthList[i] > lengthList[i + gap]:
                lengthList[i], lengthList[i + gap] = lengthList[i + gap], lengthList[i]
                barList[i], barList[i + gap] = barList[i + gap], barList[i]
                swap(barList[i], barList[i + gap])
                sorted = False
                yield
            else:
                colorBar(barList[i], "white")
            i = i + 1

# -------------------------------------------COCKTAIL SHAKER SORT------------------------------------------------

def cocktail_shaker_Sort():
    global barList
    global lengthList

    n = len(lengthList)
    swapped = True
    while swapped:
        swapped = False
        for i in range(1, n):
            if lengthList[i - 1] > lengthList[i]:
                lengthList[i - 1], lengthList[i] = lengthList[i], lengthList[i - 1]
                barList[i - 1], barList[i] = barList[i], barList[i - 1]
                swap(barList[i], barList[i - 1])
                swapped = True
                yield
            else:
                colorBar(barList[i - 1], "white")
        if swapped == False:
            return
        swapped = False
        for i in range(n - 1, 0, -1):
            if lengthList[i - 1] > lengthList[i]:
                lengthList[i - 1], lengthList[i] = lengthList[i], lengthList[i - 1]
                barList[i - 1], barList[i] = barList[i], barList[i - 1]
                swap(barList[i - 1], barList[i])
                swapped = True
                yield
            else:
                colorBar(barList[i], "white")

# -------------------------------------------BOGO SORT------------------------------------------------
def bogo_Sort():
    global barList
    global lengthList

    n = len(lengthList)
    gap = n

    def is_sorted(lengthList):
        for i in range(0,n-1):
            if lengthList[i] > lengthList[i+1]:
                return False
        return True

    while not is_sorted(lengthList):
        for i in range(0,n-1):
            if lengthList[i] < lengthList[i+1]:
                lengthList[i], lengthList[i] = lengthList[i -1], lengthList[i]
                barList[i], barList[i -1] = barList[i  -1], barList[i]
                random.shuffle(lengthList)
                swap(barList[i], barList[i -1])
                yield
            else:
                colorBar(barList[i], "white")
            i = i + 1

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
    sound(x)

# ===========================Function for sound=====================
def sound(size):
    # calculate note frequencies
    A_freq = 200
    size = A_freq * size ** (4 / 12)

    # get timesteps for each sample, T is note duration in seconds
    sample_rate = 44100
    T = 0.05
    t = np.linspace(0, T, int(T * sample_rate), False)

    # generate sine wave notes
    Csh_note = np.sin(size * t * 2 * np.pi)

    # concatenate notes
    audio = np.hstack(Csh_note)
    # normalize to 16-bit range
    audio *= 700 / np.max(np.abs(audio))
    # convert to 16-bit data
    audio = audio.astype(np.int16)

    # start playback
    play_obj = sa.play_buffer(audio, 1, 2, sample_rate)

    # wait for playback to finish before exiting
    # play_obj.wait_done()
# ===========================  VERIFYING IF THE BARS ARE SORTED=========================
def _verify():
    global barList
    global lengthList
    global is_verify

    for i in range(len(lengthList) - 1):
        if lengthList[i] < lengthList[i + 1]:
            colorBar(barList[i], 'green')
            sound(lengthList[i])
            yield
    colorBar(barList[-1], 'green')


def verify():
    global worker
    worker = _verify()
    animate()

# =========================== START BUTTON FUNCTION=========================
def start():
    global worker
    algo = variable.get()
    if algo == OPTIONS[0]:
        worker =  selection_Sort()
    elif algo == OPTIONS[1]:
        worker = bubble_Sort()
    elif algo == OPTIONS[2]:
        worker = insertion_Sort()
    elif algo == OPTIONS[3]:
        worker = comb_Sort()
    elif algo == OPTIONS[4]:
        worker = cocktail_shaker_Sort()
    elif algo == OPTIONS[5]:
        worker = bogo_Sort()
    animate()

# ===========================  ANIMATION FUNCTION=========================
def animate():
    global worker
    global is_verify
    if worker is not None:
        try:
            next(worker)
            root.after(scale_speed.get(), animate)
        except StopIteration:
            if not is_verify:
                verify()
                is_verify = True
            else:
                is_verify = False
                worker = None
        finally:
            root.after_cancel(animate)

# ===========================Generate=====================
colonne_size = 10
windowSize = 500
worker = None
is_verify = False

def generate():
    global barList
    global lengthList
    global colonne_size
    canvas.delete('all')
    barList = []
    lengthList = []

    colonne_size = scale.get()
    data = list(range(1, windowSize // colonne_size + 1))
    random.shuffle(data)

    for i, height in enumerate(data):
        bar = canvas.create_rectangle(i * colonne_size, windowSize - (height * colonne_size),
                                      i * colonne_size + colonne_size, windowSize,
                                      outline="black", fill="white")
        barList.append(bar)
        lengthList.append(height * colonne_size)

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
Generate = tk.Button(buttonFrame, text="Generate", width=20, font=('Times', 20), background='#C69749', highlightcolor='red', command = generate, foreground='#282A3A', relief='raised', activebackground='black', activeforeground='#C69749')
Start = tk.Button(buttonFrame, text="Start", width=20, font=('Times', 20), background='#C69749', highlightcolor='red', command = start,  foreground='#282A3A', relief='raised', activebackground='black', activeforeground='#C69749')
exit = tk.Button(buttonFrame, text="Exit", width=20, font=('Times', 20), background='#C69749', highlightcolor='red',  command=root.quit, foreground='#282A3A', relief='raised', activebackground='black', activeforeground='#C69749')

dropDown.grid(padx=15, pady=15, row=0, column=0, sticky='WE')
scale.grid(padx=15, pady=15, row=1, column=0, sticky='WE')
scale_speed.grid(padx=15, pady=15, row=2, column=0, sticky='WE')
Generate.grid(padx=15, pady=15, row=3, column=0, sticky='WE')
Start.grid(padx=15, pady=15, row=4, column=0, sticky='WE')
exit.grid(padx=15, pady=15, row=5, column=0, sticky='WE')


buttonFrame.grid(padx=15, pady=15, row=1, column=0, sticky='WE')

#For Simulation
simulationFrame = ttk.Frame(mainFrame, width=500, height=500, style='Frame4.TFrame')
canvas = tk.Canvas(simulationFrame, bg="black", height=500, width=500, highlightcolor='black')
canvas.grid(padx=15, pady=15, row=1, column=0)
simulationFrame.grid(padx=15, pady=15, row=1, column=1)

# ==========GRID CONFIGURATIONS==========

root.columnconfigure(0, weight=2)
root.rowconfigure(0, weight=2)

generate()
root.resizable(width=False, height=False)
root.mainloop()