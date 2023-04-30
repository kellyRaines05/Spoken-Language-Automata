# This project will utilize the International Phonetic Alphabet 
# to display the various translations from English, French, and
# German to IPA and light up the respective phonemes in the
# pronounciation of a word.

from tkinter import *
from tkinter import ttk, messagebox
from buttonFunctions import *
from predict import *

# verify input and selection after pressing the "GO" button
def verification():
    resultMessage.config(text = "")
    error = False

    # verify valid drop down selection
    if dropDown.get() == "Select Language...":
        error = True
    
    inputWord = input.get()
    inputWord = inputWord.strip()

    # verify valid input string
    if (len(inputWord) == 0 or len(inputWord) > 15 or inputWord.isalpha() == False):
        error = True

    if error:
        resultMessage.config(text = "Please enter only 1 word less than 15 characters (only letters) and language must be selected.")
        resultMessage.grid(row = 2, column = 0, pady = 5)
        resultMessage.config(fg = "red")
        return
    
    # start translation
    encodedInput = encodeUserInput(inputWord, dropDown.get())
    result = predict(encodedInput, dropDown.get())

    if len(result) == 0:
        messagebox.showerror("ERROR", "Error translating word to IPA. Please try again later.")
        return
    colorResultButtons(result)
    resultMessage.config(text = result)
    resultMessage.grid(row = 2, column = 0, pady = 5)
    resultMessage.config(fg = "green")


# root pane
root = Tk()
root.title("Spoken Language Automata")
root.geometry("1200x800")
root.rowconfigure(0, weight = 1)
root.columnconfigure(0, weight = 1)

# instructions/ user input area
topBox = Frame(root)
topBox.grid(row = 0, column = 0, sticky = N)
topBox.rowconfigure(0, weight = 1)
topBox.columnconfigure(0, weight = 1)
topBox.columnconfigure(1, weight = 1)
topBox.columnconfigure(2, weight = 1)

# IPA Display area
bodyFrame = Frame(root, width = 1200, height = 800)
bodyFrame.grid(row = 0, column = 0)
bodyFrame.rowconfigure(0, weight = 1)
bodyFrame.columnconfigure(0, weight = 1)
bodyFrame.columnconfigure(1, weight = 1)
bodyFrame.columnconfigure(2, weight = 1)
bodyFrame.columnconfigure(3, weight = 1)
bodyFrame.columnconfigure(4, weight = 1)
bodyFrame.columnconfigure(5, weight = 1)

vowelFrame = Frame(bodyFrame, relief= "ridge", borderwidth = 5, width = 600, height = 600)
vowelFrame.grid(row = 0, column = 0, ipady = 15, ipadx = 15, padx = 10, columnspan = 3, sticky = EW)
consonantFrame = Frame(bodyFrame, relief = "ridge", borderwidth = 5, width = 600, height = 600)
consonantFrame.grid(row = 0, column = 3, ipadx = 15, padx = 10, columnspan = 3, sticky = EW)

vowelBox = Frame(vowelFrame)
vowelBox.grid(row = 0, column = 0)
vowelBox.rowconfigure(0, weight = 1)
vowelBox.rowconfigure(1, weight = 1)
vowelBox.rowconfigure(2, weight = 1)
vowelBox.rowconfigure(3, weight = 1)
vowelBox.columnconfigure(0, weight = 1)
vowelBox.columnconfigure(1, weight = 1)
vowelBox.columnconfigure(2, weight = 1)
vowelBox.columnconfigure(3, weight = 1)
vowelBox.columnconfigure(4, weight = 1)
vowelBox.columnconfigure(5, weight = 1)
vowelBox.columnconfigure(6, weight = 1)
vowelBox.columnconfigure(7, weight = 1)

consonantBox = Frame(consonantFrame)
consonantBox.grid(row = 0, column = 0)
consonantBox.rowconfigure(0, weight = 1)
consonantBox.rowconfigure(1, weight = 1)
consonantBox.rowconfigure(2, weight = 1)
consonantBox.rowconfigure(3, weight = 1)
consonantBox.rowconfigure(4, weight = 1)
consonantBox.rowconfigure(5, weight = 1)
consonantBox.columnconfigure(0, weight = 1)
consonantBox.columnconfigure(1, weight = 1)
consonantBox.columnconfigure(2, weight = 1)
consonantBox.columnconfigure(3, weight = 1)
consonantBox.columnconfigure(4, weight = 1)
consonantBox.columnconfigure(5, weight = 1)
consonantBox.columnconfigure(6, weight = 1)
consonantBox.columnconfigure(7, weight = 1)
consonantBox.columnconfigure(8, weight = 1)
consonantBox.columnconfigure(9, weight = 1)
consonantBox.columnconfigure(10, weight = 1)
consonantBox.columnconfigure(11, weight = 1)
consonantBox.columnconfigure(12, weight = 1)
consonantBox.columnconfigure(13, weight = 1)
consonantBox.columnconfigure(14, weight = 1)

Label(topBox, text = "Please enter a word: ", font = "Times 12 bold").grid(row = 0, column = 0, pady = 5, sticky = N)
resultMessage = Label(topBox, text = "", font = "Times 15 bold")

# user input
input = Entry(topBox, width = 80)
input.insert(0, "Type here...")
input.grid(row = 1, column = 0, padx = 5)

# drop down
dropDown = ttk.Combobox(topBox, state = "readonly", values = ["English", "French", "German"])
dropDown.set("Select Language...")
dropDown.grid(row = 1, column = 1, padx = 5)
dropDown.bind("<<ComboboxSelected>>", highlightButtons)

# button initiates machine
enterButton = Button(topBox, text = "GO", command = verification)
enterButton.grid(row = 1, column = 2, padx = 5, ipadx = 10)
root.bind("<Return>", verification)

# phoneme (vowel and consonant box) contents
Label(vowelBox, text = "Vowel Phonemes", font = "Times 15 bold").grid(row = 0, column = 2, pady = 5, columnspan = 3)
Label(consonantBox, text = "Consonant Phonemes", font = "Times 15 bold").grid(row = 0, column = 5, pady = 5, columnspan = 5)

# grid shows international phonetic alphabet
placePhoneme(vowelBox = vowelBox, consonantBox = consonantBox)

root.mainloop()