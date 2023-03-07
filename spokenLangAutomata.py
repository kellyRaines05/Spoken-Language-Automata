# This project will utilize the International Phonetic Alphabet 
# to display the various translations from English, French, and
# German to IPA and light up the respective phonemes in the
# pronounciation of a word

from tkinter import *
from tkinter.ttk import *
import tkinter as tk

# root pane
root = tk.Tk()
root.title("Spoken Language Automata")
width, height = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry("%dx%d+0+0" % (width,height))
# root.configure(background="light blue") change color

# user input
input = tk.Text(root, height = 1, width = 100)
input.pack(padx = 5, pady = 10, side = CENTER)

# drop down
options = ["Select Language", "English", "French", "German"]
clicked = StringVar()
clicked.set("Select Language...")

dropDown = OptionMenu(root, clicked, *options)
dropDown.pack(padx = 5, pady = 10, side = CENTER)


# to do translation function
def getIPA():
    pass

# button initiates machine
enterButton = tk.Button(root, text = "GO", command = getIPA)
enterButton.pack(padx = 5, pady = 10, side = CENTER)

# grid shows international phonetic alphabet



#tk.Label(root, text = "Enter word: ", font ="Times 12 bold")




root.mainloop()